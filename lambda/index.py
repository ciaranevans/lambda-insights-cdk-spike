import os
from datetime import datetime
from io import BytesIO

import boto3

BUCKET = os.environ["BUCKET"]


def handler(event, context):
    io_stream = BytesIO()
    io_stream.write(os.urandom(1024 * 1024 * 1024))
    io_stream.seek(0)
    s3_client = boto3.client("s3")
    s3_client.upload_fileobj(
        io_stream, BUCKET, datetime.now().strftime("%Y-%m-%d-%H%M%S")
    )
