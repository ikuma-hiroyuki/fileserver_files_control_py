import os
import shutil
from datetime import datetime
from pathlib import Path

import dotenv

if 9 <= datetime.now().hour <= 22:
    dotenv.load_dotenv()

    backup_dir = Path(os.getenv('ZAIKO_BACKUP_DIR'))
    target_file = Path(os.getenv('ZAIKO_TARGET_FILE'))

    now = datetime.now().strftime('%Y%m%d%H%M')
    backup_file = backup_dir / f'{target_file.stem}_{now}{target_file.suffix}'

    shutil.copy(target_file, backup_file)
