from fastapi import APIRouter
from uuid import UUID
from api.controllers.user_controller import UserController
from api.services.user_service import UserService
from api.config.config import config
from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.app_response import AppResponse

router = APIRouter()

# Initialize UserController with UserService
user_service = UserService(session=AsyncSession())  # Pass your session here
user_controller = UserController(user_service)

# Routes for CRUD operations
@router.post("/users")
async def create_user(name: str):
    return await user_controller.create_user(name)

@router.get("/users/{user_id}")
async def get_user(user_id: UUID):
    return await user_controller.get_user(user_id)

@router.get("/users")
async def get_all_users():
    return await user_controller.get_all_users()

@router.put("/users/{user_id}")
async def update_user(user_id: UUID, name: str):
    return await user_controller.update_user(user_id, name)

@router.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    return await user_controller.delete_user(user_id)
