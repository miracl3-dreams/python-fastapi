from fastapi import HTTPException, status
from api.services.user_service import UserService
from api.utils.app_response import AppResponse
from uuid import UUID

class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def create_user(self, name: str):
        user = await self.user_service.create_user(name)
        return AppResponse.send_success(data={"user": user}, message="User created successfully")

    async def get_user(self, user_id: UUID):
        user = await self.user_service.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return AppResponse.send_success(data={"user": user})

    async def get_all_users(self):
        users = await self.user_service.get_all_users()
        return AppResponse.send_success(data={"users": users})

    async def update_user(self, user_id: UUID, name: str):
        user = await self.user_service.update_user(user_id, name)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return AppResponse.send_success(data={"user": user}, message="User updated successfully")

    async def delete_user(self, user_id: UUID):
        success = await self.user_service.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return AppResponse.send_success(message="User deleted successfully")
