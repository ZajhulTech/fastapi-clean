from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class MongoBaseModel(BaseModel):
    """
    Clase base para todos los modelos de Pydantic que interactúan
    con MongoDB. Contiene la configuración general para el manejo del ID
    y los tipos.
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {str: str}