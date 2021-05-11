FROM python:3.8.0-slim
RUN apt-get update && apt-get install gcc -y && apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --user -r requirements.txt
ADD generate_data.py /home/generate_data.py
ENTRYPOINT [ "python3", "/home/generate_data.py" ]
