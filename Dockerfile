# docker build -t cutthroat-site .

# FROM the official NiceGUI image
FROM zauberzeug/nicegui:latest

WORKDIR /app

# copy & install your Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
