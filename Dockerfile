FROM debian:latest
RUN apt-get update && apt-get install -y python3.11 less nano && apt-get clean
ADD main.py ./
ADD inpt.py ./
ADD hi.txt ./
ADD hihello.txt ./
ADD LICENSE ./
CMD ["python3.11", "./main.py"]
