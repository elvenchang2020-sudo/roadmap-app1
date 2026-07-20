FROM python:3.14-slim
WORKDIR /app1/collecting
COPY . .
RUN pip3 install -r requirments.txt
CMD ["python3","log_collector.py"]