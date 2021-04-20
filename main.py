from fastapi import FastAPI
# from Authentication.router import router as auth_router
from Controller.Router import data_router
import uvicorn


def get_application() -> FastAPI:
    application = FastAPI()
    # application.include_router(auth_router)
    application.include_router(data_router)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
