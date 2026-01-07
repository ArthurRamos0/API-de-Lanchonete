from fastapi import APIRouter
from schemas.produto_schema import ProdutoCreate
from services.produto_service import listar_produtos, cadastrar_produto

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


@router.get("/")
def get_produtos():
    return listar_produtos()


@router.post("/", status_code=201)
def create_produto(produto: ProdutoCreate):
    return cadastrar_produto(
        produto.nome,
        produto.preco,
        produto.estoque
    )
