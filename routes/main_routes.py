from fastapi import APIRouter
from fastapi import FastAPI, status, HTTPException, Depends, Query
from pydantic import BaseModel
from typing import Annotated, Optional, List
import models
from connection.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


base_routes = APIRouter()

db_dependencies = Annotated[Session, Depends(get_db)]


# Pydantic models for request and response
class SingleCustomer(BaseModel):
    customer_name: str

    class Config:
        extra = "forbid"


class SingleOrder(BaseModel):
    customer_id: int
    order_date: Optional[datetime] = datetime.now()

    class Config:
        extra = "forbid"


class CustomerResponse(BaseModel):
    customer_id: int
    customer_name: str


class OrderResponse(BaseModel):
    order_id: int
    customer_id: int
    order_date: datetime


@base_routes.post(
    "/customer/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED
)
async def add_customer(customer: SingleCustomer, db: db_dependencies):
    new_customer = models.Customers(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)  # Refresh to get the customer ID
    return new_customer


@base_routes.get("/customers/{customer_id}", response_model=CustomerResponse)
async def get_customer(customer_id: int, db: db_dependencies):
    customer = (
        db.query(models.Customers)
        .filter(models.Customers.customer_id == customer_id)
        .first()
    )
    if customer is None:
        raise HTTPException(
            status_code=404, detail=f"Customer with id {customer_id} does not exist"
        )
    return customer


@base_routes.put("/customer/{customer_id}", response_model=CustomerResponse)
async def update_customer(
    customer_id: int, customer: SingleCustomer, db: db_dependencies
):
    db_customer = (
        db.query(models.Customers)
        .filter(models.Customers.customer_id == customer_id)
        .first()
    )
    if db_customer is None:
        raise HTTPException(
            status_code=404, detail=f"Customer with id {customer_id} does not exist"
        )

    db_customer.customer_name = customer.customer_name
    db.commit()
    db.refresh(db_customer)
    return db_customer


@base_routes.delete("/customer/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int, db: db_dependencies):
    db_customer = (
        db.query(models.Customers)
        .filter(models.Customers.customer_id == customer_id)
        .first()
    )
    if db_customer is None:
        raise HTTPException(
            status_code=404, detail=f"Customer with id {customer_id} does not exist"
        )

    db.delete(db_customer)
    db.commit()
    return


@base_routes.post(
    "/order/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED
)
async def add_order(order: SingleOrder, db: db_dependencies):
    try:
        new_order = models.Orders(**order.dict())
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return new_order


@base_routes.get("/order/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: db_dependencies):
    order = db.query(models.Orders).filter(models.Orders.order_id == order_id).first()
    if order is None:
        raise HTTPException(
            status_code=404, detail=f"Order with id {order_id} does not exist"
        )
    return order


@base_routes.get(
    "/customers", response_model=List[CustomerResponse], status_code=status.HTTP_200_OK
)
async def list_customers(db: db_dependencies):
    customers = db.query(models.Customers).all()
    return customers


@base_routes.get(
    "/customers/{customer_id}/orders",
    response_model=List[OrderResponse],
    status_code=status.HTTP_200_OK,
)
async def list_customer_orders(customer_id: int, db: db_dependencies):
    db.query(models.Customers).filter(
        models.Customers.customer_id == customer_id
    ).first()
    orders = (
        db.query(models.Orders).filter(models.Orders.customer_id == customer_id).all()
    )
    if not orders:
        raise HTTPException(
            status_code=404,
            detail=f"No orders found for customer with id {customer_id}",
        )
    return orders
