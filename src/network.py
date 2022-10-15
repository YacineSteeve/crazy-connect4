import os
import sys
import boto3
from botocore.exceptions import NoCredentialsError

from src.logger import logger, ROOT_DIR, LOG_FILE, USER_INFO
from src import utils

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

if not ACCESS_KEY or not SECRET_KEY:
    with open(os.path.join(ROOT_DIR, '.env')) as file:
        ACCESS_KEY = file.readline().strip()[11:]
        SECRET_KEY = file.readline().strip()[11:]


def upload_to_aws(local_file, bucket, s3_file):
    logger.info(f'Start uploading {s3_file} to AWS')
    s3 = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        logger.debug("Upload Successful")
        return True
    except FileNotFoundError:
        logger.warning(f'The file {local_file} was not found')
        return False
    except NoCredentialsError:
        logger.error("Credentials are invalid or not available")
        return False
    except:
        logger.error("Something went wrong while uploading")
        return False


if __name__ == '__main__':
    uploaded = upload_to_aws(LOG_FILE, 'cc4bucket', f'{USER_INFO}_{utils.TIME}')
