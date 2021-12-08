__all__ = ["create_server"]

from fastapi.applications import FastAPI

def create_server(debug_: bool) -> FastAPI:

    server = FastAPI(debug=debug_, openapi_url=None)

    return server
