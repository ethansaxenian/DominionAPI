from collections.abc import Generator

from deta import Base, Deta, Drive

from app.core.config import settings

deta = Deta(settings.DETA_PROJECT_KEY)

db = deta.Base(settings.DETA_BASE_NAME)


def get_db() -> Generator[Base, None, None]:
    yield db


drive = deta.Drive(settings.DETA_DRIVE_NAME)


def get_drive() -> Generator[Drive, None, None]:
    yield drive
