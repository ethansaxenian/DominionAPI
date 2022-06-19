from dataclasses import dataclass
from typing import Optional, Union

from fastapi import Depends, Query
from google.cloud.firestore_v1 import AsyncClient
from sqlalchemy.orm import Session

from core.config import Settings, get_settings
from db import get_db


@dataclass
class CommonParams:
    include_b64: Optional[bool]
    settings: Settings
    db: Union[Session, AsyncClient]


async def common_parameters(
    include_b64: Optional[bool] = Query(
        default=False,
        description="Whether to include base64-encoded images in the response. Defaults to false.",
        alias="include-b64",
    ),
    global_settings: Settings = Depends(get_settings),
    db: Union[Session, AsyncClient] = Depends(get_db),
) -> CommonParams:
    return CommonParams(include_b64=include_b64, settings=global_settings, db=db)