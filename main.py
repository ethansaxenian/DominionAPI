from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from api import api_router
from core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    contact={"name": settings.AUTHOR_NAME, "email": settings.AUTHOR_EMAIL},
    license_info={"name": settings.LICENSE},
)

app.include_router(api_router, prefix=settings.API_PREFIX)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def base():
    return RedirectResponse(url="/docs")
