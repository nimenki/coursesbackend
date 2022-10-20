FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app/src/"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
