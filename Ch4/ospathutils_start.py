#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("item exists: " + str(path.exists("textfile.txt")))
    print("item is a file: " + str(path.isfile("textfile.txt")))
    print("item is a directory: " + str(path.isdir("textfile.txt")))

    # Work with file paths
    print("item path: " + str(path.realpath("textfile.txt")))
    print("item path and name : " + str(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
    t = time.ctime((path.getmtime("textfile.txt")))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item was modified
    mod = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("The item was modified", mod, "hours ago")
    print("Or,", mod.total_seconds(), "seconds ago")


if __name__ == "__main__":
    main()
