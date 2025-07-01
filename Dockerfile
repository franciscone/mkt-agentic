FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential curl

WORKDIR /mkt-agentic

COPY . .

RUN pip install --trusted-host files.pythonhosted.org \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]
