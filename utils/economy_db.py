from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import asyncio
import config
import discord

class EconomyDB:
    def __init__(self):
        self.cluster = AsyncIOMotorClient(config.mongodb_link)
        self.economy = self.cluster["economy"]
    
    async def insert_member(self, *, member):
        if await self.economy["balances"].find_one({"_id": member.id}) is None:
            new_member = {}
            new_member["cash"] = 0
            new_member["bank"] = 0
            await self.economy.insert_one(new_member)
            return True
        else:
            return False
    
    async def add_money(self, *, member, mode = "cash", value):
        await self.insert_member(member = member)
        await self.economy.update_one(
            {"_id": member.id},
            {"$inc": {mode: value}}
        )
        return True
    
    async def remove_money(self, *, member, mode = "cash", value):
        await self.insert_member(member = member)
        await self.economy.update_one(
            {"_id": member.id},
            {"$dec": {mode: value}}
        )
        return True
    
    async def get_money(self, *, member):
        await self.insert_member(member = member)
        return await self.economy["balances"].find_one({"_id": member.id})