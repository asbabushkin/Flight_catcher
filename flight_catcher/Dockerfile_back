FROM python:3.10-alpine
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
WORKDIR /app
COPY ./flight_catcher/ ./flight_catcher/
COPY ./flight_search/ ./flight_search/
COPY ./static/ ./static/
COPY data.py manage.py entrypoint.sh ./
EXPOSE 8000
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "/app/entrypoint.sh"]