import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:bhassurance@localhost:3306/ListeNat')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
