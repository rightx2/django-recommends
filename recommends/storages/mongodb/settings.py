from django.conf import settings

RECOMMENDS_STORAGE_MONGODB_DATABASE_DEFAULT = {
    'HOST': 'localhost',
    'PORT': 27017,
    'NAME': 'recommends',
}
RECOMMENDS_STORAGE_MONGODB_DATABASE = getattr(settings, 'RECOMMENDS_STORAGE_MONGODB_DATABASE', RECOMMENDS_STORAGE_MONGODB_DATABASE_DEFAULT)
RECOMMENDS_STORAGE_MONGODB_SIMILARITY_COLLECTION = getattr(settings, 'RECOMMENDS_STORAGE_MONGODB_SIMILARITY_COLLECTION', 'similarity')
RECOMMENDS_STORAGE_MONGODB_RECOMMENDATION_COLLECTION = getattr(settings, 'RECOMMENDS_STORAGE_MONGODB_RECOMMENDATION_COLLECTION', 'recommendation')
RECOMMENDS_STORAGE_MONGODB_FSYNC = getattr(settings, 'RECOMMENDS_STORAGE_MONGODB_FSYNC', False)
