from pydantic import BaseModel, Field
from datetime import datetime


class VendaCreate(BaseModel):
    produto_id: int = Field(..., gt=0, example=1)
    quantidade: int = Field(..., gt=0, example=2)


class VendaResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    total: float
    data: datetime
