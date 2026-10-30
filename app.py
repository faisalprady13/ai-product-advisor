from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Product(BaseModel):
    name: str
    brand: str | None = None
    price: float | None = None
    currency: str | None = None
    ram_gb: int | None = None
    storage_gb: int | None = None


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/products")
def create_product(product: Product):
    return product


@app.post("/products/cheapest")
def cheapest_product(products: list[Product]):
    if not products:
        return None

    return min(products, key=lambda product: product.price or float("inf"))
