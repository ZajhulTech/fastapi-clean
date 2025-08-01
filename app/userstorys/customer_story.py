# from app.interfaces.userstorys.user_story import IUserStory
from app.models.response.customer_response import CustomerResponse
from app.infra.api.response import Response
from app.interfaces.database.base_repository import IBaseRepository
from app.interfaces.userstorys.customer_story import ICustomerStory
from typing import List, Optional

class CustomerStory(ICustomerStory):
    def __init__(self, repo: IBaseRepository):
       pass
       #self.repo = repo
       # self.customer_repo = MongoRepository(self.repo.collection, CustomerModel)
    
    async def get_customer(self, phone: Optional[str] = None) -> Response[List[CustomerResponse]]:
       
       # customer = await self.customer_repo.find_one({"_id": user_id}) if user_id else None
        response = Response[List[CustomerResponse]]

        result = Response.with_data(response)
        return result
