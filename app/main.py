import markdown
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from core.config import get_settings
from db import create_db_and_tables

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    contact={"name": settings.AUTHOR_NAME, "email": settings.AUTHOR_EMAIL},
    license_info={"name": settings.LICENSE},
)

app.include_router(api_router, prefix=settings.API_PREFIX)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def readme():
    readme_file = open(f"{settings.ROOT_DIR}/README.md", "r")
    markdown_str = markdown.markdown(readme_file.read(), extensions=["fenced_code"])
    html = BeautifulSoup(markdown_str, "html.parser")
    for tag in html.find_all("a"):
        tag["rel"] = "noopener noreferrer"
        tag["target"] = "_blank"
    return html.prettify()
