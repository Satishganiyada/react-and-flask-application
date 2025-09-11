# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app


RUN pip install Flask

# Copy app code
COPY . .

# Create upload directory inside container
RUN mkdir -p uploads

# Expose Flask default port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
