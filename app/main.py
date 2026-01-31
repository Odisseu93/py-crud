from fastapi import FastAPI

app = FastAPI()

from orders.routes import orders_router

# inlude the routes
app.include_router(order_router)


# runnig the server
# uvicorn main:app --reload