import sys

import pandas
import pathlib
import os


while True:
    text = open("export_service.txt", "r")
    content = text.read()
    if content == "run":
        directory = pathlib.Path.home() / "Downloads"  # Change this value to export elsewhere
        csv_file_path = str(directory) + "/locationlist.csv"
        text = pandas.read_csv("data.txt", delimiter="/")
        if os.path.exists(csv_file_path):
            i = 1
            csv_file_path = str(directory) + "/locationlist(" + str(i) + ").csv"
            while os.path.exists(str(directory) + "/locationlist(" + str(i) + ").csv"):
                i += 1
                csv_file_path = str(directory) + "/locationlist(" + str(i) + ").csv"
        text.to_csv(csv_file_path, index=None)
        text = open("export_response.txt", "w")
        text.write(".csv exported to " + str(directory))
        text.close()

        text = open("export_service.txt", "w")
        text.close()
    elif content == "terminate":
        text = open("export_service.txt", "w")
        text.close()
        sys.exit()
