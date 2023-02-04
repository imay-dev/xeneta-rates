import logging

from fastapi import FastAPI

from app.api import ping, rates

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI(title = "Xeneta Rates")
    application.include_router(ping.router)
    application.include_router(
        rates.router, prefix="/rates", tags=["rates"]
    )

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
