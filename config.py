import os
class Config():
    """General configuration class"""
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://anilla:Busolo@1997@localhost/blog'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
config_options={
'development':DevConfig,
'production':ProdConfig
}
