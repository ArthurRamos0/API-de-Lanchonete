from pydantic import BaseModel, Field


class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=2, example="Hambúrguer")
    preco: float = Field(..., gt=0, example=15.90)
    estoque: int = Field(..., ge=0, example=10)


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True
