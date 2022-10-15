from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import asyncio
import config
import discord

class GiveawaysDB:
    def __init__(self):
        self.cluster = AsyncIOMotorClient(config.mongodb_link)
        self.giveaways = self.cluster.giveaways.giveaways_list
    
    async def insert_giveaway(
        self, *, 
        message_id: int, 
        channel_id: int, 
        prize: str, 
        end_time: int
    ) -> bool:
        if await self.giveaways.find_one({"_id": message_id}) is not None:
            await self.giveaways.inset_one({
                "_id": message_id,
                "channel_id": channel_id,
                "prize": prize,
                "end_time": end_time
            })
            
            return True
            
        else:
            return False   
            
    async def delete_giveaway(
        self, *, 
        message_id: int
    ) -> bool:
        if await self.giveaways.find_one({"_id": message_id}) is None:
            await self.giveaways.delete_one({"_id": message_id})
            
            return True
            
        else:
            return False
