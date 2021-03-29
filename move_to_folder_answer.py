import os
import sys

directory = "images/physics"
folders = [x[0].replace("\\", "/") for x in os.walk(directory)][1:]
print(folders)

for file in os.listdir(directory):
    if file.endswith("." + "png".upper()):
        for folder in folders:
            if os.path.isfile(folder + "/" + file) and folder.split("/")[-1] != "answers":
                print(folder, file)
                os.rename(directory + "/" + file, folder + "/answers/" + file)
