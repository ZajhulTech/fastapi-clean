from typing import List
from fastapi import APIRouter, Depends
from app.models.request.user_request import UserCreateRequest
from app.models.response.customer_response import CustomerResponse
from motor.motor_asyncio import AsyncIOMotorClient
from app.userstorys.customer_story import CustomerStory
#from app.infra.database.mongo_repository import MongoRepository
from app.infra.api.response_utils import get_response, get_custom_response
from app.infra.api.response import Response
from app.interfaces.userstorys.customer_story import ICustomerStory

import os

router = APIRouter()
base = "/customer"
Tag = "Customers"

def get_user_story() -> ICustomerStory:
    return CustomerStory(None)

##def get_user_repo():
##    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
##    return MongoUserRepository(client)

@router.get(base, response_model=Response[List[CustomerResponse]], tags=[Tag])
async def get_customer(user_story: ICustomerStory = Depends(get_user_story)):
    
    return await user_story.get_customer()
 