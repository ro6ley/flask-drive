import os
import tempfile

from flask import Flask, render_template, request, redirect
from s3_demo import list_files, upload_file
from werkzeug.utils import secure_filename


BUCKET=os.getenv('BUCKET')

app = Flask(__name__)

@app.route('/')
def storage():
    contents = list_files(BUCKET)
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        # create a temporary directory using the context manager
        with tempfile.TemporaryDirectory() as dir:
            print('created temporary directory', dir)
            path = os.path.join(dir, secure_filename(f.filename))
            f.save(path)
            upload_file(path, BUCKET, secure_filename(f.filename))
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
