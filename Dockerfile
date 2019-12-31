FROM python:3.7
WORKDIR /flask-s3-upload

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

EXPOSE 5000

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]