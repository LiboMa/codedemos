FROM python:2.7
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask run"]
