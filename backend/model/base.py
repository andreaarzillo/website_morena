from sqlalchemy import Column, Integer, String

from backend.repository.main_repository import Base


class Data(Base):
    __tablename__ = "data"
    # id = Column(Integer, primary_key=True, index=True)
    # age = Column(Integer)
    # clinical_stage_T = Column(Integer)
    # clinical_stage_N = Column(Integer)
    # clinical_stage_M = Column(Integer)
    # overall_stage = Column(String)
    # histology = Column(String)
    # gender = Column(String)
    # survival_time = Column(Integer)
    # dead_status = Column(Integer)
