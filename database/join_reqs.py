# Don't Remove Credit Tg - @Silando
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Freenethubtech
# Ask Doubt on telegram @Silando

# Clone Code Credit : YT - @Freenethubtech / TG - @Silando / GitHub - @Anony101

import motor.motor_asyncio
from info import AUTH_CHANNEL, OTHER_DB_URI

class JoinReqs:

    def __init__(self):
        if OTHER_DB_URI:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(OTHER_DB_URI)
            self.db = self.client["JoinReqs"]
            self.col = self.db[str(AUTH_CHANNEL)]
        else:
            self.client = None
            self.db = None
            self.col = None

    def isActive(self):
        if self.client is not None:
            return True
        else:
            return False

    async def add_user(self, user_id, first_name, username, date):
        try:
            await self.col.insert_one({"_id": int(user_id),"user_id": int(user_id), "first_name": first_name, "username": username, "date": date})
        except:
            pass

    async def get_user(self, user_id):
        return await self.col.find_one({"user_id": int(user_id)})

    async def get_all_users(self):
        return await self.col.find().to_list(None)

    async def delete_user(self, user_id):
        await self.col.delete_one({"user_id": int(user_id)})

    async def delete_all_users(self):
        await self.col.delete_many({})

    async def get_all_users_count(self):
        return await self.col.count_documents({})
