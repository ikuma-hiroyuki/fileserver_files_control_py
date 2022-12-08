import os
from datetime import datetime
from pathlib import Path

import dotenv

dotenv.load_dotenv()

backup_dir = Path(os.getenv('ZAIKO_BACKUP_DIR'))
today = datetime.now().strftime('%Y%m%d')

for file in backup_dir.glob('*.xls*'):
    file_date = datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y%m%d')
    if file_date <= today:
        os.chmod(file, 755)
        file.unlink()
