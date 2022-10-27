import secrets

from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader

from core.config import settings

api_key_header_auth = APIKeyHeader(
    name=settings.API_KEY_NAME,
    description="API Key, required for all POST, PUT, and DELETE operations.",
    auto_error=False,
)


async def get_api_key(api_key_header: str = Security(api_key_header_auth)):
    if isinstance(api_key_header, str) and secrets.compare_digest(
        api_key_header, settings.API_KEY
    ):
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key"
        )
