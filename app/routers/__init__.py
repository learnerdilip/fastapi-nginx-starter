from fastapi import APIRouter
from .user import router as user_router
from .auth import router as auth_router
from .heartbeat import router as heartbeat_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(user_router, prefix="/users", tags=["User"])
router.include_router(heartbeat_router, prefix="", tags=["Heartbeat"])
