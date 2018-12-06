import os


class Config:
    DEBUG = False
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = os.getenv('DB_NAME')


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DB_NAME = os.getenv('DB_TEST_NAME')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DB_NAME = os.getenv('DB_NAME')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
