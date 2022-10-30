import os
from typing import Literal

from filestack import Client

from src.utils import TIME, USER_INFO, ROOT_DIR
from src.logger import LOG_FILE

CLIENT = Client('AL127UDBTiTs6PuhL6K1Qz')

STORE_PARAMS = {
    'mimetype': 'text/plain',
    'location': 's3',
    'path': '/'
}


def upload_file(file_type: Literal['logs', 'games']) -> str:
    """This function send logs file and game stats file to be stored on https://dev.filestack.com/ .

    Args:
        file_type (str): Tells whether the logs or the game stats are to be uploaded.

    Returns:
        str: The url to the uploaded file.

    """
    if file_type == 'logs':
        file = LOG_FILE.replace(USER_INFO, f'{USER_INFO}_{TIME}')
        os.rename(LOG_FILE, file)
        STORE_PARAMS['path'] = f'Logs/{USER_INFO}/'
    elif file_type == 'games':
        temp_file = os.path.join(ROOT_DIR, 'games.csv')
        file = temp_file[:-4] + f'_{TIME}.csv'
        os.rename(temp_file, file)
        STORE_PARAMS['mimetype'] = 'text/csv'
        STORE_PARAMS['path'] = 'Games/'
    else:
        file = 'empty.txt'

    try:
        link = CLIENT.upload(filepath=file, store_params=STORE_PARAMS)
        os.remove(file)
    except Exception as error:
        raise error

    return link.url


if __name__ == '__main__':
    file_link = upload_file('logs')
