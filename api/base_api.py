from fastapi import FastAPI

from settings import ROOT_DIR
from api.user_api.authentication import router as auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.get("/info")
async def root():
    with open(ROOT_DIR / "README.md", "r", encoding='utf8') as readme:
        readme_content = readme.read()

    return {"info about the project": readme_content}
