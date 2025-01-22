from api.repositories.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

class UserService:
    def __init__(self, session: AsyncSession):
        self.user_repository = UserRepository(session)

    async def create_user(self, name: str):
        return await self.user_repository.create_user(name)

    async def get_user(self, user_id: uuid.UUID):
        return await self.user_repository.get_user_by_id(user_id)

    async def get_all_users(self):
        return await self.user_repository.get_all_users()

    async def update_user(self, user_id: uuid.UUID, name: str):
        return await self.user_repository.update_user(user_id, name)

    async def delete_user(self, user_id: uuid.UUID):
        return await self.user_repository.delete_user(user_id)
