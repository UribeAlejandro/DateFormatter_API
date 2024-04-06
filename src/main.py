import logging

from fastapi import FastAPI

from src.routes import counter, date, index

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(date.router, tags=["date"])
    application.include_router(index.router, tags=["index"])
    application.include_router(counter.router, tags=["counter"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
