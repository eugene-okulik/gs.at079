FROM jenkins/jenkins:lts-jdk21

USER root

# Устанавливаем Python, pip, wget
RUN apt-get update && apt-get install -y python3 python3-pip wget python3-venv

# Устанавливаем Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Устанавливаем ChromeDriver
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/linux64/chromedriver-linux64.zip \
    && apt-get install -y unzip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Рабочая директория
WORKDIR /home/jenkins/

# Копируем файлы
COPY test_pack.py .
COPY requirements.txt .

# Устанавливаем Python зависимости (в виртуальном окружении)
RUN pip install --no-cache-dir -r requirements.txt

# Создаем папку для тестов
RUN mkdir -p /home/jenkins/tests

# Переменные окружения
ENV COOL_PORT=8080
ENV COOL_IP=0.0.0.0
ENV COOL_LOG=logs

USER jenkins

# Порты
EXPOSE 50000/tcp
EXPOSE 8080/tcp