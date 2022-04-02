from flask import Flask

from backend.controller.main_controller import main_controller

app = Flask(__name__)
app.register_blueprint(main_controller)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///patients_database.db"
# db_alchemy = SQLAlchemy(app)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == '__main__':
    #     # db_lite.create()
    #     # db_lite.populate_people()
    #     # db_lite.populate_images()
    app.run(debug=True)
