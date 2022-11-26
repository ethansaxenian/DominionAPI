from deta import Deta

from core.config import settings

deta = Deta(settings.DETA_PROJECT_KEY)

db = deta.Base(settings.DETA_BASE_NAME)


def get_db():
    yield db


drive = deta.Drive(settings.DETA_DRIVE_NAME)


def get_drive():
    yield drive
