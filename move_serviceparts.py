import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv

from smtp import send_mail

load_dotenv()


def move_file():
    serviceparts_dir = Path(os.getenv('SERVICE_PARTS_DIR'))
    server_file = serviceparts_dir / os.getenv('FILE_NAME')
    backup_dir = serviceparts_dir / 'backup'
    box_file = box_dir / os.getenv('FILE_NAME')

    yesterday = datetime.today() - timedelta(days=1)

    if server_file.exists():
        shutil.copy(server_file, backup_dir / f'{box_file.stem}_{yesterday.strftime("%Y%m%d")}{box_file.suffix}')

        # box_fileが存在していたら追記
        if box_file.exists():
            with open(box_file, 'a', encoding='utf-8') as f:
                with open(server_file, 'r', encoding='utf-8') as f2:
                    f.write(f2.read())
            os.remove(server_file)
        else:
            shutil.move(server_file, box_file)
    else:
        send_mail('😱BOXアップロード失敗', 'SOKEN.txtがありません')


if __name__ == '__main__':
    box_dir = Path(os.getenv('BOX_DIR'))
    if not box_dir.exists():
        send_mail('😱BOXアップロード失敗', 'BOXにログインできません')
    else:
        # 月曜日から金曜日のみ実行
        if datetime.today().weekday() < 5:
            move_file()
