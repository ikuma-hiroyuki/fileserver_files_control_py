import os
import shutil
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
box_dir = Path(os.getenv('BOX_DIR'))
box_file = box_dir / os.getenv('FILE_NAME')
server_file = serviceparts_dir / os.getenv('FILE_NAME')

# box_fileが存在していたらコピー (server_fileが存在していればcreate_serviceparts_tsv_pyでSOKEN.txtに追記する)
if box_file.exists():
    shutil.copy(server_file, box_dir / server_file.name)
else:
    shutil.move(server_file, box_dir / server_file.name)
