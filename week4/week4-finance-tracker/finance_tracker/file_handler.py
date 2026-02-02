import json
import shutil
import os

FILE_PATH = "data/expenses.json"
BACKUP_DIR = "data/backup/"
EXPORT_DIR = "data/exports/"


def ensure_dirs():
    os.makedirs("data", exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(EXPORT_DIR, exist_ok=True)


def load_expenses():
    ensure_dirs()
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    ensure_dirs()
    with open(FILE_PATH, "w") as f:
        json.dump(expenses, f, indent=4)


def backup_data():
    ensure_dirs()
    if os.path.exists(FILE_PATH):
        shutil.copy(FILE_PATH, BACKUP_DIR + "expenses_backup.json")


def export_to_csv(expenses):
    ensure_dirs()
    with open(EXPORT_DIR + "expenses.csv", "w") as f:
        f.write("Date,Category,Description,Amount\n")
        for e in expenses:
            f.write(f"{e.date},{e.category},{e.description},{e.amount}\n")
