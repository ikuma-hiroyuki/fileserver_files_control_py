import os
import shutil
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
box_dir = Path(os.getenv('BOX_DIR'))

for file in serviceparts_dir.glob('*.txt'):
    shutil.move(file, box_dir / file.name)
