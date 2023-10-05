FROM debian:latest
RUN apt-get update && apt-get install -y python3.11 less nano && apt-get clean
ADD main.py ./
ADD inpt.py ./
ADD hi.txt ./
CMD ["python3", "./main.py"]
