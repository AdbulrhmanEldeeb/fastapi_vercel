from sqlalchemy import Column, String, Integer, ForeignKey, DATE
from sqlalchemy.orm import relationship
from connection.database import Base


class Customers(Base):
    __tablename__ = "customers"

    # Primary keys are automatically indexed by default,
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(50), nullable=False)

    orders = relationship("Orders", back_populates="customer")


class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(DATE, nullable=True)

    customer = relationship("Customers", back_populates="orders")
