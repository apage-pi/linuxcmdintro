FROM python:latest
ADD main.py ./
ADD inpt.py ./
ADD hi.txt ./
CMD ["python", "./main.py"]
