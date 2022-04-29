import pydantic



from typing import Optional
from pydantic import BaseModel

class Super(BaseModel):
    id: Optional[str]
    name:str
    age:int
    country:str
    superpower:str
    universe:str
