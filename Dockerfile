FROM python:3.6
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#ENTRYPOINT ["python"]
#CMD ["flask run"]
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
