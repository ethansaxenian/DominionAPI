import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api import api_router
from core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    contact={"name": settings.AUTHOR_NAME, "email": settings.AUTHOR_EMAIL},
    license_info={"name": settings.LICENSE},
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def readme():
    readme_file = open(f"{settings.ROOT_DIR}/README.md", "r")
    markdown_str = markdown.markdown(readme_file.read(), extensions=["fenced_code"])
    return markdown_str
