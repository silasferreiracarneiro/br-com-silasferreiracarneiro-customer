FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

COPY . /code/

# Install dependencies
RUN pip install uvicorn 
RUN pip install -r requirements.txt

EXPOSE 8000