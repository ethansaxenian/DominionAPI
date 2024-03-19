from collections.abc import Generator

from deta import Deta
from deta.base import _Base
from deta.drive import _Drive

from app.core.config import settings

deta = Deta(settings.DETA_PROJECT_KEY)

db = deta.Base(settings.DETA_BASE_NAME)
drive = deta.Drive(settings.DETA_DRIVE_NAME)


def get_db() -> Generator[_Base, None, None]:
    yield db


def get_drive() -> Generator[_Drive, None, None]:
    yield drive
