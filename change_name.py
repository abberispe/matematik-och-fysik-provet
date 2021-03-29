import os
import sys

year = sys.argv[1]

for file in os.listdir("images/physics"):
    if file.endswith("." + "png".upper()):
        path_file = "images/physics/" + file
        print(path_file)
        print(file.split(".")[0] + "_" + str(year))
        os.rename(path_file, "images/physics/" + file.split(".")[0] + "_" + str(year) + ".PNG")