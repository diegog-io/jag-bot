FROM python:alpine

RUN adduser -S build -G wheel
USER build
WORKDIR /home/build/app

COPY requirements.txt .

RUN pip3 install --no-cache-dir --no-warn-script-location -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "src/bot.py" ]