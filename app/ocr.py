import os
import time
from file_conversion import convert_files_to_docs_patch


def run_ocr():

    # get the total size in mb and file count of the 'files' directory
    total_size = 0
    total_files = 0
    print(f"Getting file count and size...")
    for dirpath, dirnames, filenames in os.walk("/files"):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            total_files += 1
    #print(f"Total files: {total_files}")
    #print(f"Total size: {total_size / 1024 / 1024} MB")

    if total_files == 0:
        print("No files to convert!!!")
        exit()

    print(f"Converting files...")
    start = time.time()
    convert_files_to_docs_patch("/files")
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    print(f"est time per file: {(end - start) / total_files} seconds")
    print(f"est bytes per second: {total_size / (end - start)} bytes/s")
    print(
        f"est time to ocr 2.5TB: {(2.5 * 1024 * 1024 * 1024 * 1024) / (total_size / (end - start)) / 60 / 60 / 24} days"
    )
