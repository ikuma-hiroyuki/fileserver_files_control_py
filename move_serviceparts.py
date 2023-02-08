import os
import shutil
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
server_file = serviceparts_dir / os.getenv('FILE_NAME')
backup_dir = serviceparts_dir / 'backup'

box_dir = Path(os.getenv('BOX_DIR'))
box_file = box_dir / os.getenv('FILE_NAME')

shutil.copy(server_file, backup_dir / f'{box_file.stem}_{datetime.today().strftime("%Y%m%d")}{box_file.suffix}')

# box_fileが存在していたらコピー (server_fileが存在していればcreate_serviceparts_tsv_pyでSOKEN.txtに追記する)
if box_file.exists():
    shutil.copy(server_file, box_file)
else:
    shutil.move(server_file, box_file)

