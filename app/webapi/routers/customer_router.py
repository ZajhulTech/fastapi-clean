from typing import List
from fastapi import APIRouter, Depends
from app.models.response.customer_response import CustomerResponse
from motor.motor_asyncio import AsyncIOMotorClient
from app.userstorys.customer_story import CustomerStory
from app.interfaces.userstorys.customer_story import ICustomerStory
from app.infra.api.response_utils import get_response, get_custom_response
from app.infra.api.response import Response
from app.infra.mongodb.mongo_unit_of_work import MongoUnitOfWork
from dotenv import load_dotenv
import os


load_dotenv() 

router = APIRouter()
base = "/customer"
Tag = "Customers"

def get_unit_of_work() -> MongoUnitOfWork:
    mongo_uri = os.getenv("MONGODB_URI")
    client = AsyncIOMotorClient(mongo_uri)
    return MongoUnitOfWork(client)

def get_user_story(uow = Depends(get_unit_of_work)) -> ICustomerStory:
    return CustomerStory(uow) # pyright: ignore[reportArgumentType]

##def get_user_repo():
##    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
##    return MongoUserRepository(client)

@router.get(base, response_model=Response[List[CustomerResponse]], tags=[Tag])
async def get_customer(user_story: ICustomerStory = Depends(get_user_story)):
    
    return await user_story.get_customer()
 