from pydantic import BaseModel

class Item(BaseModel):
    id: int
    titulo: str
    prioridade: str
    data: str
