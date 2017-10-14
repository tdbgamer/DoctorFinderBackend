class Config:
    pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI='FILL_IN_AFTER_MAKING_PROD_DB'

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
