import random, string
from flask import Flask, request, Response
from filters import file_type
from resources import get_bucket, get_buckets_list, get_s3_config
from flask_restplus import Resource, Api, Namespace, fields
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
app.secret_key = 'flask-s3-restplus'

api = Api(app, version='0.1', title='Flask S3 Upload API',
    description='Flask S3 Upload API')

ns = api.namespace('upload', description='upload images to s3')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

# 允许上传的图片类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# generate random file name
def random_name():
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

@ns.route('/')
@ns.expect(upload_parser)
class Upload(Resource):
    def post(self):
        if 'file' not in request.files:
            return {
                'status': 'fail',
                'message': 'no set file'
            }

        file = request.files["file"]
        if file.filename == '':
            return {
                'status': 'fail',
                'message': 'no set filename'
            }

        if not allowed_file(file.filename):
            allowed_file_ext = ','.join(ALLOWED_EXTENSIONS)
            return {
                'status': 'fail',
                'message': 'only support file extension:' + allowed_file_ext,
                'data': allowed_file_ext
            }

        if file and allowed_file(file.filename):

            mime = file.filename.rsplit(".")[1]
            file_key = random_name() + "." + mime

            my_bucket = get_bucket()
            my_bucket.Object(file_key).put(Body=file,ContentType=file_type(file.filename))
            return {
                'status': 'success',
                'message': 'upload file success',
                'data': file_key
            }

@ns.route('/config')
class Config(Resource):
    def get(self):
        return get_s3_config()

if __name__ == "__main__":
    app.run()
