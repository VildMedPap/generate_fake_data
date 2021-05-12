FROM python:3.8.0-slim
RUN apt-get update && apt-get install gcc -y && apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --user --no-cache -r requirements.txt
COPY . .
VOLUME [ "/data" ]
ENTRYPOINT [ "python3", "generate_data.py" ]