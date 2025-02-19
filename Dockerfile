# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import nltk; nltk.download('vader_lexicon')"

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]