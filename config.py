import os

class Config:
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_DATABASE}'.format(
        DB_USERNAME=os.getenv('DB_USERNAME'),
        DB_PASSWORD=os.getenv('DB_PASSWORD'),
        DB_HOST=os.getenv('DB_HOST'),
        DB_DATABASE=os.getenv('DB_DATABASE')
    )

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
