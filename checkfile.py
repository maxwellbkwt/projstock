import os

path = "/Users/nick/Desktop/2454.csv"

#if ( os.path.isfile(path)):
#    print("file exists!")
#else:
#    print("file not found...")

def file_exists(path):
    try:
        st = os.stat(path)
    except os.error:
        return False

    return True