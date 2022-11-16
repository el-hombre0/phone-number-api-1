FROM python:3.10.6-alpine3.16
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "main.py" ]