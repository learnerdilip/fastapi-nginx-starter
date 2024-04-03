from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging

from .routers import router

from .seeder.users import seed_users
from .seeder.roles import seed_roles

from app.services.database import get_db, engine
from app.models import Base

app = FastAPI()

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def seed_database():
    # since we are using the generator outside of path operations,
    # we need to next it to get the actual session
    session_generator = get_db()
    session = next(session_generator)
    try:
        seed_roles(session)
        seed_users(session)
    finally:
        session.close()


async def startup_event():
    # to create the initial database tables and seed them
    Base.metadata.create_all(bind=engine)
    seed_database()


@router.get("/")
async def confirm_running_server():
    return {"message": "Welcome to ryberg backend server."}


app.add_event_handler("startup", startup_event)

app.include_router(router)
