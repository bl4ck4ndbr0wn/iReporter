import os


class Config:
    DEBUG = False
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    UPLOAD_FOLDER = "upload/img"
    # Database
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    # User
    SEED_ADMIN_EMAIL = os.getenv('SEED_ADMIN_EMAIL')
    SEED_ADMIN_PASSWORD = os.getenv('SEED_ADMIN_PASSWORD')
    SEED_ADMIN_USERNAME = os.getenv('SEED_ADMIN_USERNAME')
    # Flask-Mail.
    MAIL_DEFAULT_SENDER = 'contact@ireporter.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('EMAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    # Twilio SMS
    ACCOUNT_SID = os.getenv('ACCOUNT_SID')
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')
    DEFAULT_PHONE_NUMBER = os.getenv("DEFAULT_PHONE_NUMBER")


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
