import csv
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

# Path to CSV File
DATA_DIR_PATH = Path(__file__).resolve().parents[2] / "data"
CSV_PATH = DATA_DIR_PATH / "school_data.csv"


def retrieve_school_data():
    # If the CSV File doesn't exist, download and unzip it
    if not CSV_PATH.exists():
        print(f"CSV File not found at {CSV_PATH}, downloading it now...")
        response = urlopen("https://nces.ed.gov/ccd/data/zip/sl051bai_csv.zip")
        with ZipFile(BytesIO(response.read())) as zipf:
            archive_name = zipf.namelist()[0]
            zipf.extract(archive_name, DATA_DIR_PATH)
            archive_path = DATA_DIR_PATH / archive_name
            archive_path.replace(CSV_PATH)

    with open(CSV_PATH, mode="r", encoding="utf-8", errors="replace") as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            yield row
