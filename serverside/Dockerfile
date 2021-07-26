FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install -y python3
RUN apt install -y python3-pip

WORKDIR /app

COPY . .

RUN chmod 755 deploy.sh

RUN ["sh", "-c", "deploy.sh"]

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]
