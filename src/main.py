from fastapi import FastAPI

from typing import Union
import asyncio

from fastapi import FastAPI, HTTPException
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from dotenv import load_dotenv
load_dotenv()

import logging
from opentelemetry import trace
from azure.monitor.opentelemetry import configure_azure_monitor
configure_azure_monitor()
logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    logger.warning("Hello World")
    with tracer.start_as_current_span("root_request"):
        await asyncio.sleep(1)
        logger.warning("In span")
    return {"Hello": "World"}

FastAPIInstrumentor.instrument_app(app)
