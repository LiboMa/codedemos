FROM python:3.6
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["flask run"]
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
