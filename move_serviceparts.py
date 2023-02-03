import os
import shutil
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
box_dir = Path(os.getenv('BOX_DIR'))
file = serviceparts_dir / os.getenv('FILE_NAME')

# fileが存在していたらコピー (create_serviceparts_tsv_pyでSOKEN.txtに追加するためのフラグ)
if file.exists():
    shutil.copy(file, box_dir / file.name)
else:
    shutil.move(file, box_dir / file.name)
