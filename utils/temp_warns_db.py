from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import asyncio
import config
import discord

class TempWarnsDB:
    def __init__(self):
        self.cluster = AsyncIOMotorClient(config.mongodb_link)
        self.warns = self.cluster["warns"]["temp_warns"]
    
    async def insert_warn(self, *, author, member, duration):
        if await self.warns.find_one({"_id": member.id}) is None:
            new_warn = {}
            new_warn["_id"] = member.id
            new_warn["author"] = author.id
            new_warn["duration"] = duration
            await self.warns.insert_one(new_warn)
            return True
        else:
            return False

    async def remove_warn(self, *, member):
        if await self.warns.find_one({"_id": member.id}) is not None:
            await self.warns.delete_one({"_id": member.id})
            return True
        else:
            return False

    async def get_warn(self, *, member):
        return await self.warns.find_one({"_id": member.id})
    
    async def get_warns(self):
        return self.warns.find()