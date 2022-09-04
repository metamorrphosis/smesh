import pymongo
import config

class DataBase:
    def __init__(self):
        self.cluster = pymongo.MongoClient("mongodb+srv://bebroid:G4OkpALTJyAe2rlG@smeshcluster.hmfuskg.mongodb.net/?retryWrites=true&w=majority")
    
    def insert_ticket(self, ticket_id, author, who_claimed, open_time):
        new_ticket = {}
        new_ticket["_id"] = int(ticket_id)
        new_ticket["author"] = int(author.id)
        new_ticket["who_claimed"] = int(who_claimed.id)
        new_ticket["open_time"] = int(open_time)
        self.cluster["tickets"]["tickets_list"].insert_one(new_ticket)
        return True
    
    def get_ticket_id(self, ticket_channel):
        return int(''.join(x for x in ticket_channel.name if x.isdigit()))
    
    def new_claimed_member(self, member):
        if self.cluster["tickets"]["claimed_count"].find_one({"_id": member.id}) is None:
            new_member = {}
            new_member["_id"] = member.id
            new_member["all_claimed"] = 0
            new_member["temp_claimed"] = 0
            self.cluster["tickets"]["claimed_count"].insert_one(new_claimed_member)
            return True
        else:
            return False
    
    def get_claimed_data(self, member):
        self.new_claimed_member(member)
        return self.cluster["tickets"]["claimed_count"].find_one({"id": member.id})
            
       
    def claim_ticket(self, ticket_channel, who_claimed):
        self.new_claimed_member(who_claimed)
        self.cluster["tickets"]["claimed_count"].update_one({"_id": who_claimed.id}, {"$inc": {"all_claimed": 1, "temp_claimed": 1}})
        ticket_id = self.get_ticket_id(ticket_channel)
        self.cluster["tickets"]["tickets_list"].update_one({"_id": ticket_id}, {"$set": {"who_claimed": who_claimed.id}})
        return True
