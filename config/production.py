from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x08\xe9pX\xeb\x19c\x1f\xc2`\xd4\x89\x8c\xdf\x8f\x8d'