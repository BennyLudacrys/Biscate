class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3300/service-service'


class ProductionConfig(Config):
    # Configurações para produção (exemplo)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3300/service-service'


configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # Configuração padrão
}
