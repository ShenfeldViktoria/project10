
from pathlib import Path
import csv

def read_csv_file(file_path: Path) -> list[list[str]]:
    rows = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        rows.extend(csv_reader)
    return rows

if __name__ == "__main__":
    path_to_file = Path('file.csv')
    csv_data = read_csv_file(path_to_file)
    print(csv_data)
    #file_path: Path — это путь к файлу
    #Path  — это класс который упрощает работу с путями 
    #csv — это стандартный модуль для работы с CSV-файлами