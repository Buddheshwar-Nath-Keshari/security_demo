# Use Debian as base image
FROM debian:latest

# Install dependencies
RUN apt update && apt install -y python3 python3-pip python3-venv

ENV APP_ENV=production
ENV DATABASE_URL=mysql://user:password@db:3306/mydb
ENV AWS_KEY = ASDFGTRERTYUJHG34567UYHGTG

# Set up a virtual environment
RUN python3 -m venv /venv

# Install FastAPI and Uvicorn inside the virtual environment
RUN /venv/bin/pip install fastapi uvicorn requests

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app/

# Expose the API port
EXPOSE 8000


# Create a non-root user and group
# RUN groupadd appgroup && useradd -m -g appgroup appuser
# # Copy application code
# COPY --chown=appuser:appgroup . /app/
# # Switch to the non-root user
# USER appuser


# Command to start FastAPI
CMD ["/venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]