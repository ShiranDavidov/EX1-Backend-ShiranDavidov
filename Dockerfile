FROM python:3.8
RUN pip install httpx
COPY ./main.py .
CMD ["python", "./main.py"]
