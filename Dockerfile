FROM python:3.10-alpine

COPY getgrades.py .
COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "getgrades.py"]