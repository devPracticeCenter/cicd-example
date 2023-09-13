FROM python:3.10.12

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]