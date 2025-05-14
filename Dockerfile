# File: Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]


# File: .dockerignore
__pycache__/
*.pyc
*.pyo
*.pyd
.env
*.DS_Store
data/orders.json


# File: requirements.txt (if not already updated)
streamlit
pytest

# Optional AI add-on library (for future use)
openai
scikit-learn
pandas
