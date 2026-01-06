from fastapi import APIRouter, HTTPException
from schemas.venda_schema import VendaCreate
from services.venda_service import registrar_venda

router = APIRouter(
    prefix="/vendas",
    tags=["Vendas"]
)


@router.post("/", status_code=201)
def create_venda(venda: VendaCreate):
    try:
        return registrar_venda(venda.produto_id, venda.quantidade)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
