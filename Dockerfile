# Don't Remove Credit Tg - @Silando
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Freenethubtech
# Ask Doubt on telegram @Silando

# Clone Code Credit : YT - @Freenethubtech / TG - @Silando / GitHub - @Anony101

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /VJ-FILTER-BOT
WORKDIR /VJ-FILTER-BOT
COPY . /VJ-FILTER-BOT
CMD ["python", "bot.py"]
