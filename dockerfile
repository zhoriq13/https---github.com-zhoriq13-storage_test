FROM ubuntu
RUN apt-get update -y
RUN apt-get install -y python3.10 python3-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]