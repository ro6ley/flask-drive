import boto3


def upload_file(file_name, bucket, object_name=""):
    """
    Function to upload a file to an S3 bucket
    """
    if not object_name:
        object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response


def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            # https://stackoverflow.com/questions/52342974/serve-static-files-in-flask-from-private-aws-s3-bucket
            item["url"] = s3.generate_presigned_url(
                'get_object', Params = {'Bucket': bucket, 'Key': item['Key']},
            )
            contents.append(item)
    except Exception as e:
        print(e)

    return contents
