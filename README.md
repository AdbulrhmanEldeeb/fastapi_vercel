# Customer Management System

This project provides a simple and user-friendly frontend for managing customers and their orders using a FastAPI backend. The frontend is built using plain HTML, CSS, and JavaScript.

## Features

- Add a new customer
- Get customer details by ID
- Update customer details
- Delete a customer
- Add a new order for a customer
- Get all orders for a specific customer

## Prerequisites
- Ensure you have a running FastAPI server with the following endpoints:
  - `POST /customer/`
  - `GET /customers/{customer_id}`
  - `PUT /customer/{customer_id}`
  - `DELETE /customer/{customer_id}`
  - `POST /order/`
  - `GET /customers/{customer_id}/orders`
  
## Usage

1. **Add Customer**: Enter the customer name and click the "Add Customer" button.
2. **Get Customer**: Enter the customer ID and click the "Get Customer" button.
3. **Update Customer**: Enter the customer ID and new customer name, then click the "Update Customer" button.
4. **Delete Customer**: Enter the customer ID and click the "Delete Customer" button.
5. **Add Order**: Enter the customer ID and click the "Add Order" button.
6. **Get Customer Orders**: Enter the customer ID and click the "Get Customer Orders" button.
