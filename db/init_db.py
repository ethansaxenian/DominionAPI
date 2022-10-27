from deta import Deta

from core.config import settings

deta = Deta(settings.DETA_BASE_PROJECT_KEY)

db = deta.Base(settings.DETA_BASE_NAME)


def get_db():
    yield db
