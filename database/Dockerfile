FROM postgres:15.8-alpine
RUN chmod +x init_db.sh
COPY ./init_db.sh /docker-entrypoint-initdb.d/init_db.sh
