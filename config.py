class Config:
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://dgukmpjsoknhpi:c36296c6182e9d163e1a7d4db18cecbb77e5b3cece2a2977af2be9a088fdfa02@ec2-23-23-248-162.compute-1.amazonaws.com:5432/daksnb3kg25trr'

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
