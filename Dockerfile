FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
# disable proxy options if you arent using it
RUN pip3 install --proxy=http://192.168.49.1:8282 --no-cache-dir -r requirements.txt

COPY ./DB ./DB/
COPY ./TesisControlDB ./TesisControlDB/
COPY "Carla" "db.sqlite3" "LsW" "manage.py" "secretaria" ./

# VOLUME ["/usr/src/app"]

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]