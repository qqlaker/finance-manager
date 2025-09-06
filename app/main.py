from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    # await db_helper.init_redis()
    yield
    # await db_helper.dispose()
    # await db_helper.close_redis()


app: FastAPI = FastAPI(lifespan=lifespan)

# app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="statics")
