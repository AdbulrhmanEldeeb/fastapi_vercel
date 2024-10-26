// scripts.js
const API_URL = 'https://fastapi-mysql-ok3a.onrender.com/';

async function getCustomer() {
    const id = document.getElementById('get-customer-id').value;
    try {
        const response = await fetch(`${API_URL}/customers/${id}`);
        const customer = await response.json();
        displayResult(`ID: ${customer.customer_id}, Name: ${customer.customer_name}`);
    } catch (error) {
        displayResult('Customer not found.');
    }
}

async function addCustomer() {
    const customer = {
        customer_name: document.getElementById('add-customer-name').value,
    };

    try {
        const response = await fetch(`${API_URL}/customer/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(customer),
        });
        const newCustomer = await response.json();
        displayResult(`Added: ID: ${newCustomer.customer_id}, Name: ${newCustomer.customer_name}`);
    } catch (error) {
        displayResult('Error adding customer.');
    }
}

async function updateCustomer() {
    const id = parseInt(document.getElementById('update-customer-id').value);
    const customer = {
        customer_name: document.getElementById('update-customer-name').value,
    };

    try {
        const response = await fetch(`${API_URL}/customer/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(customer),
        });
        const updatedCustomer = await response.json();
        displayResult(`Updated: ID: ${updatedCustomer.customer_id}, Name: ${updatedCustomer.customer_name}`);
    } catch (error) {
        displayResult('Error updating customer.');
    }
}

async function deleteCustomer() {
    const id = parseInt(document.getElementById('delete-customer-id').value);

    try {
        await fetch(`${API_URL}/customer/${id}`, {
            method: 'DELETE',
        });
        displayResult('Customer deleted successfully.');
    } catch (error) {
        displayResult('Error deleting customer.');
    }
}

async function addOrder() {
    const order = {
        customer_id: parseInt(document.getElementById('order-customer-id').value),
    };

    try {
        const response = await fetch(`${API_URL}/order/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(order),
        });
        const newOrder = await response.json();
        displayResult(`Added Order: ID: ${newOrder.order_id}, Customer ID: ${newOrder.customer_id}, Date: ${newOrder.order_date}`);
    } catch (error) {
        displayResult('Error adding order.');
    }
}

async function getCustomerOrders() {
    const customerId = document.getElementById('orders-customer-id').value;
    try {
        const response = await fetch(`${API_URL}/customers/${customerId}/orders`);
        const orders = await response.json();
        displayResult(`Orders for Customer ${customerId}: ${JSON.stringify(orders)}`);
    } catch (error) {
        displayResult('Error fetching orders.');
    }
}

function displayResult(message) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>${message}</p>`;
}
