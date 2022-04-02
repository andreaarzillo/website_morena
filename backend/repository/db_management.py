import os
import sqlite3

import pandas as pd

db = "patients_database.db"
patients_info = "/dataset/manifest-1603198545583/NSCLC Radiomics Lung1.clinical-version3-Oct 2019.csv"
images_root = "/dataset/manifest-1603198545583/NSCLC-Radiomics"


def create():
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS patients (
        [id] INTEGER PRIMARY KEY,
        [age] INTEGER,
        [clinical_stage_T] INTEGER,
        [clinical_stage_N] INTEGER,
        [clinical_stage_M] INTEGER,
        [overall_stage] TEXT,
        [histology] TEXT,
        [gender] TEXT,
        [survival_time] INTEGER,
        [dead_status] INTEGER )
        """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS scans (
        [id] INTEGER PRIMARY KEY,
        [scan] TEXT,
        [patient_id] INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (id))
        """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS tags (
        [id] INTEGER PRIMARY KEY,
        [tag.py] TEXT,
        [patient_id] INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (id))
        """)

    conn.commit()
    conn.close()


def populate_people():
    conn = sqlite3.connect(db)
    c = conn.cursor()

    df = pd.read_csv(os.getcwd() + patients_info)
    df = df.fillna(-1)

    for i in range(len(df)):
        id = i + 1
        age = int(df.loc[i, "age"])
        clinical_stage_T = int(df.loc[i, "clinical.T.Stage"])
        clinical_stage_N = int(df.loc[i, "Clinical.N.Stage"])
        clinical_stage_M = int(df.loc[i, "Clinical.M.Stage"])
        overall_stage = df.loc[i, "Overall.Stage"]
        histology = df.loc[i, "Histology"]
        gender = df.loc[i, "gender"]
        survival_time = int(df.loc[i, "Survival.time"])
        dead_status = int(df.loc[i, "deadstatus.event"])

        params = id, age, clinical_stage_T, clinical_stage_N, clinical_stage_M, overall_stage, histology, gender, \
                 survival_time, dead_status

        c.execute("""INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", params)

    conn.commit()
    conn.close()


def populate_images():
    conn = sqlite3.connect(db)
    c = conn.cursor()

    # os.chdir(images_root)

    for root, subdirs, files in os.walk(os.getcwd() + images_root):
        # for i in range(422):
        #     print(subdirs[i])
        print(root)

    # params = 1
    #
    # c.execute("""INSERT INTO scans VALUES (?, ?, ?)""", params)
    #
    # conn.commit()
    conn.close()
