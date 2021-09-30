[![HitCount](http://hits.dwyl.io/ro6ley/flask-drive.svg)](http://hits.dwyl.io/ro6ley/flask-drive)

# FlaskDrive 

This repository contains the code for this [blogpost](https://stackabuse.com/file-management-with-aws-s3-python-and-flask/) on [StackAbuse](https://stackabuse.com/).

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [AWS CLI Tool](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository

```
$ git clone https://github.com/ro6ley/flask-drive.git
```

2. Check into the cloned repository

```
$ cd flask-drive
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:

```
$ pipenv install && pipenv shell
```

4. Install the requirements

```
$ pip install -r requirements.txt
```

4. Configure AWS CLI

```
$ aws configure
```

5. Create a bucket on AWS Dashboard and update it on the `app.py` file on line 10.

6. Run the application

```sh
$ BUCKET="insert_bucket_name_here" FLASK_APP=app.py FLASK_RUN_PORT=8080 FLASK_ENV=development FLASK_RUN_HOST=0.0.0.0 flask run
```

7. Navigate to http://localhost:8080/storage


## Docker container

Required to have docker, git.

### How to run the container locally

```sh
docker build -t flask-drive .
docker run -p 5000:5000 -d -e AWS_ACCESS_KEY_ID="<Your_Access_Key>" -e AWS_SECRET_ACCESS_KEY="<Your_Secret_Key>" -e BUCKET="<Your_Bucket_Name>" flask-drive
```

Navigate to http://localhost:5000/storage

### Common errors

1. Bind for 0.0.0.0:5000 failed: port is already allocated

select a different port, "docker run -p 8080:5000"
Navigate to http://localhost:8080/storage

## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
