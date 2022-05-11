import os
from flask import Blueprint, cli
from flask_sqlalchemy import SQLAlchemy
from app import config

db = SQLAlchemy()
database = Blueprint('database', __name__,)


@database.cli.command('create')
def init_db():
    db.create_all()


@database.before_app_first_request
# Holds uploaded files
def create_upload_folder():
    root = config.Config.BASE_DIR
    # Sets the name of the apps log folder to logs
    uploadfolder = os.path.join(root,'..',config.Config.UPLOAD_FOLDER)
    # Makes a directory if it doesn't exist
    if not os.path.exists(uploadfolder):
        os.mkdir(uploadfolder)
    db.create_all()
