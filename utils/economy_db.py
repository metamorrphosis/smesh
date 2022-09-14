from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import asyncio
import config
import discord

class EconomyDB:
    def __init__(self):
        self.cluster = AsyncIOMotorClient(config.mongodb_link)
        self.economy = self.cluster["economy"]
    
    async def inser_member(self, *, member):
        if await self.economy["balances"].find_one({"_id": member.id}) is None:
            new_member = {}
            new_member["r"] = aaaa
            return True
        else:
            return False
    
