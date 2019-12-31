# Flask S3 Restplus Upload
Base on boto3, flask-restplus aws s3 upload API.

## Usage
### 1. copy .env.sample to .env, set your config.
```
cp .env.sample .env
```

set your config in `.env`.

### 2. install python lib dependency
```
pip install -r requirements.txt

```

### 3. run on local machine
set flask env.
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

run
```
flask run
```

### Deploy
1. build docker image
```
docker build -t flask-s3-uplaod .
```

2. run docker(in server)
```
docker run --env-file ./.env -p 5000:80 flask-s3-upload
```
