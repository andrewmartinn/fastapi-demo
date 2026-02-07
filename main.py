from fastapi import FastAPI
from app.routes.posts import router as posts_router

# init fastapi
app = FastAPI()

# health api
@app.get("/health")
def health_check():
    return {"status": "ok"}

# app routes
app.include_router(posts_router)

