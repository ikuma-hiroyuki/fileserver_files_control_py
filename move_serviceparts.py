import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from line_notify import line_notify

load_dotenv()

serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
server_file = serviceparts_dir / os.getenv('FILE_NAME')
backup_dir = serviceparts_dir / 'backup'

box_dir = Path(os.getenv('BOX_DIR'))
box_file = box_dir / os.getenv('FILE_NAME')

yesterday = datetime.today() - timedelta(days=1)

file_util_type = ''
if server_file.exists():
    shutil.copy(server_file, backup_dir / f'{box_file.stem}_{yesterday.strftime("%Y%m%d")}{box_file.suffix}')

    # box_fileが存在していたら追記
    if box_file.exists():
        with open(box_file, 'a', encoding='utf-8') as f:
            with open(server_file, 'r', encoding='utf-8') as f2:
                f.write(f2.read())
        file_util_type = 'append'
        os.remove(server_file)
    else:
        shutil.move(server_file, box_file)
        file_util_type = 'move'
else:
    file_util_type = 'server file not exist'

line_notify(file_util_type)
