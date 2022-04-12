from fastapi import FastAPI
import logging
from starlette.requests import Request
from starlette_context import middleware, plugins, context
from starlette.responses import JSONResponse
import time
logger = logging.getLogger(__name__)

app = FastAPI()

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    return {
        "client_host": request.client.host,
        "time": time.time().__str__(),
        "Address": request.base_url,
        "headers": request.headers,
        "cookies": request.cookies,
        "path": request.url.path,
        "query_params": request.query_params,
        "path_params": request.path_params,
        "client_port": request.client.port,
        "host": request.client.host
        }
