import os


class Config:
    DEBUG = False
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    # Database
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    # User
    SEED_ADMIN_EMAIL = os.getenv('SEED_ADMIN_EMAIL')
    SEED_ADMIN_PASSWORD = os.getenv('SEED_ADMIN_PASSWORD')
    SEED_ADMIN_USERNAME = os.getenv('SEED_ADMIN_USERNAME')


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
