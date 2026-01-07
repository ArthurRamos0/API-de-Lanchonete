
from fastapi import FastAPI
from routers import produtos, vendas

app = FastAPI(title="API de Lanchonete")

app.include_router(produtos.router)
app.include_router(vendas.router)
