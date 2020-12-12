class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        # 'db': 'develop_danmemo',
        # 'host': '127.0.0.1',
        # 'port': 27017
        'host': 'mongodb://localhost:27017/develop_danmemo'
    }
    
class TestinConfig(Config):
    DEBUG = False
    
config = {
    'test': TestinConfig,
    'development': DevelopmentConfig
}
