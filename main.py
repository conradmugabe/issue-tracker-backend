"""entry point"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """healthcheck"""
    return {"status": "ok"}
