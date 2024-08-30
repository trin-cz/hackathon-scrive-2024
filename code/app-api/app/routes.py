from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
import logging

from . import graphql, init

logger = logging.getLogger(__name__)

#### Routes ####

app = FastAPI()

@app.on_event("startup")
async def reinit():
    init.init()

@app.post("/api/callback", response_class=Response)
async def document_callback(request: Request):
    body = await request.body()
    logger.info(body)

app.include_router(graphql.get_app(), prefix="/api")