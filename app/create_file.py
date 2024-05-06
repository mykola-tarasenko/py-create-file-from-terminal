import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory",
                    type=str, nargs="*", help="creates directory")
parser.add_argument("-f", "--file", type=str, help="creates a file")

args = parser.parse_args()

if args.directory:
    os.makedirs(os.path.join(*args.directory), exist_ok=True)
if args.file:
    with open(os.path.join(*args.directory or "", args.file), "a") as file:
        file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
        line_number = 1
        while True:
            data = input("Enter content line: ")
            if data == "stop":
                file.write("\n\n")
                break
            file.write(f"\n{line_number} {data}")
            line_number += 1
