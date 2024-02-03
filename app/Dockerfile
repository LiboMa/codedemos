FROM python:3.6
COPY . /app
WORKDIR /app
#ENV FLASK_APP=app.py
ENV FLASK_APP=app.py
RUN pip install --upgrade pip && pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
#RUN pip install -r requirements.txt 
#ENTRYPOINT ["python"]
#CMD ["flask run"]
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
