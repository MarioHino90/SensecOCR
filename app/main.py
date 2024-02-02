print("starting")

from postgres import create_tables

print("loaded postgres")

from ocr import run_ocr

print("loaded ocr")

create_tables()
print("Tables created")

# path = last_path()
# print(f"Last path: {path}")
# exit()
# create skip table

print("Running OCR")
run_ocr()

print("OCR complete")

print("Done")
