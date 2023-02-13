import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from line_notify import line_notify

load_dotenv()

serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
server_file = serviceparts_dir / os.getenv('FILE_NAME')
backup_dir = serviceparts_dir / 'backup'

box_dir = Path(os.getenv('BOX_DIR'))
box_file = box_dir / os.getenv('FILE_NAME')

shutil.copy(server_file, backup_dir / f'{box_file.stem}_{datetime.today().strftime("%Y%m%d")}{box_file.suffix}')

file_util_type = ''

# box_fileが存在していたらコピー (server_fileが存在していればcreate_serviceparts_tsv_pyでSOKEN.txtに追記する)
if box_file.exists():
    shutil.copy(server_file, box_file)
    file_util_type = 'copy'
else:
    shutil.move(server_file, box_file)
    file_util_type = 'move'

line_notify(file_util_type)
