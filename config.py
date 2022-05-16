import os
class Config:
    '''
    General configuration parent class
    '''
 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/bikes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Bike Hire'
    SENDER_EMAIL = 'loisemulwa7@gmail.com'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/bikes'
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
       
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}


# import os
# # import smtplib , ssl
# # from dotenv import load_dotenv
# # load_dotenv()
# class Config:
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#     SQLALCHEMY_TRACK_MODIFICATIONS=True
#     SECRET_KEY=os.environ.get('SECRET_KEY')
#     # UPLOADED_PHOTOS_DEST ='app/static/photos'
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 456
#     MAIL_USE_TLS = False
#     MAIL_USE_SSL = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
# class ProdConfig(Config):
#     # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
#     uri = os.getenv('DATABASE_URL')
#     if uri and uri.startswith('postgres://'):
#         uri = uri.replace('postgres://', 'postgresql://', 1)
#     SQLALCHEMY_DATABASE_URI = uri
# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/bikes'
#     DEBUG = True
# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }









