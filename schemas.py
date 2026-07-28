from pydantic import BaseModel
class mobileCreate(BaseModel):
    name: str
    department:str
    location:str
    email:str
    


class mobileResponse(mobileCreate):
    id: int

    model_config = {
        "from_attributes": True
    }