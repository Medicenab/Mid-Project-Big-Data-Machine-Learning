from tiangolo/uvicorn-gunicorn-fastapi:python3.9

add ./ /miapi

workdir /miapi

run pip install -r requirements.txt

env PORT=8080

cmd uvicorn main:app --host 0.0.0.0 --port=${PORT}
