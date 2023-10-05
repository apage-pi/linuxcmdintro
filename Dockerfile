FROM python:latest
ADD main.py ./
ADD inpt.py ./
CMD ["python", "./main.py"]
