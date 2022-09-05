from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import config

class TicketsDB:
    def __init__(self):
        self.cluster = AsyncIOMotorClient(config.mongodb_link)
    
    async def insert_ticket(self, *, author, who_claimed = None, open_time):
        await self.cluster["tickets"]["ticets_list"].update_one({"_id": 0}, {"$inc": {"nmr": 1}})
        ticket_id = await self.cluster["tickets"]["tickets_list"].find_one({"_id": 0})
        print(ticket_id)
        new_ticket = {}
        new_ticket["_id"] = ticket_id
        new_ticket["author"] = int(author.id)
        new_ticket["who_claimed"] = int(who_claimed.id) if who_claimed else 0
        new_ticket["open_time"] = int(open_time)
        await self.cluster["tickets"]["tickets_list"].insert_one(new_ticket)
        return ticket_id
    
    def get_ticket_id(self, ticket_channel):
        return int(''.join(x for x in ticket_channel.name if x.isdigit()))
    
    async def new_claimed_member(self, member):
        if self.cluster["tickets"]["claimed_count"].find_one({"_id": member.id}) is None:
            new_member = {}
            new_member["_id"] = member.id
            new_member["all_claimed"] = 0
            new_member["temp_claimed"] = 0
            await self.cluster["tickets"]["claimed_count"].insert_one(new_claimed_member)
            return True
        else:
            return False
    
    async def get_claimed_data(self, member):
        await self.new_claimed_member(member)
        return self.cluster["tickets"]["claimed_count"].find_one({"id": member.id})
            
       
    async def claim_ticket(self, ticket_channel, who_claimed):
        await self.new_claimed_member(who_claimed)
        await self.cluster["tickets"]["claimed_count"].update_one({"_id": who_claimed.id}, {"$inc": {"all_claimed": 1, "temp_claimed": 1}})
        ticket_id = self.get_ticket_id(ticket_channel)
        await self.cluster["tickets"]["tickets_list"].update_one({"_id": ticket_id}, {"$set": {"who_claimed": who_claimed.id}})
        return True
