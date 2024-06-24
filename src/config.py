class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    ORACLE_HOST = 'localhost'
    ORACLE_USER = 'PIS'
    ORACLE_PASSWORD = 'unl123'
    ORACLE_DB = 'PIS'

config={
    'development':DevelopmentConfig,
}