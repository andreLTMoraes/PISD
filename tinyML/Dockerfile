FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY tinyMLdevice.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "tinyMLdevice.py"]

docker swarm join --token SWMTKN-1-5rlw4mbweip37ahunubi4ks1swq2t15fdku4zuyphpcl8xpdka-aah70e9d8itfk6vfqlh86n77q 192.168.0.29:2377