from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

from app.api.router import api_router
from app.core.config import settings

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
