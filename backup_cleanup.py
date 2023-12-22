import os
import datetime

backup_dir = os.getenv('BACKUP_PATH')
backup_threshold = int(os.getenv('BACKUP_RETENTION' ))

if not backup_dir:
    raise ValueError("The BACKUP_DIR environment variable is required.")

def parse_date_from_filename(filename):
    date_str = filename.split('.')[0]  # Remove the .gz extension
    return datetime.datetime.strptime(date_str, "%d%m%Y")

backup_files = [f for f in os.listdir(backup_dir) if f.endswith(".gz")]
file_dates = [(f, parse_date_from_filename(f)) for f in backup_files]

file_dates.sort(key=lambda x: x[1])

if len(file_dates) > backup_threshold:
    files_to_delete = file_dates[:len(file_dates) - backup_threshold]
    for file, _ in files_to_delete:
        file_path = os.path.join(backup_dir, file)
        print(f"Deleting old backup file: {file_path}")
        os.remove(file_path)

print("Cleanup complete.")