FROM python:3.12-slim

# Set working directory
WORKDIR /code

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8080

# Run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
CMD ["fastapi", "run", "main.py", "--port", "8080"]
