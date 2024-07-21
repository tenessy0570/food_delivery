from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.responses import JSONResponse

import config


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except SQLAlchemyError as exc:
        config.logger.error(f"A database error caught: {repr(exc)}, {request=}")
        return JSONResponse({"detail": "Internal error caught"}, status_code=500)
    except Exception as exc:
        return JSONResponse({"detail": str(exc)}, status_code=400)
