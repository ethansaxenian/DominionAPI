import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api import api_router

app = FastAPI(
    title="Dominion API",
    description="An API for the game Dominion",
    contact={"name": "Ethan Saxenian", "email": "ethansaxenian@gmail.com"},
    license_info={"name": "MIT"},
)

app.include_router(api_router)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def readme():
    readme_file = open("README.md", "r")
    markdown_str = markdown.markdown(readme_file.read(), extensions=["fenced_code"])
    return markdown_str
