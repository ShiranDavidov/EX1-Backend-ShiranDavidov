FROM python:3.8
RUN pip install httpx
COPY ./client.py .
CMD ["python", "./main.py"]