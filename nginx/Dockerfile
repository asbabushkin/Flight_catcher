FROM python:3.10-alpine AS static-builder
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
WORKDIR /app
COPY ./flight_catcher/flight_catcher/ ./flight_catcher/
COPY ./flight_catcher/flight_search/ ./flight_search/
COPY ./flight_catcher/static/ ./static/
COPY ./flight_catcher/manage.py ./
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:8000


FROM nginx:1.27
COPY --from=static-builder /app/static ./static
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d/
