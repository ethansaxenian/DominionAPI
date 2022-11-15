from dataclasses import dataclass
from typing import Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session

from core.config import Settings, settings
from db import get_db


@dataclass
class CommonParams:
    include_b64: Optional[bool]
    settings: Settings
    db: Session


def common_parameters(
    include_b64: Optional[bool] = Query(
        default=False,
        description="Whether to include base64-encoded images in the response. Defaults to false.",
        alias="include-b64",
    ),
    global_settings: Settings = Depends(lambda: settings),
    db: Session = Depends(get_db),
) -> CommonParams:
    return CommonParams(include_b64=include_b64, settings=global_settings, db=db)
