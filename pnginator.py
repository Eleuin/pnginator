from PIL import Image
import sys
import os.path

# main image decode
def decode(filepath):
    if(check_file(filepath) == True):
        print('file is good')
    else:
        print('Error: file does not exist')

# main image encode
def encode(filepath):
    if(check_file(filepath) == True):
        print('file is good')
    else:
        print('Error: file does not exist')

# check if file actually exists
# FIXME: add homedir and localdir support
def check_file(filepath):
    return os.path.isfile(filepath)

# check command line arguments
if len(sys.argv) >= 2:
    if len(sys.argv) >= 3:
        if (sys.argv[1] == '-d' or sys.argv[1] == '--decode'):
            decode(sys.argv[2])
        elif (sys.argv[1] == '-e' or sys.argv[1] == '--encode'):
            encode(sys.argv[2])
        else:
            print("Error: invalid argument")

    elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print('Usage: python pnginator.py [option]\n')
        print('Options:')
        print('-v, --version             show version')
        print('-h, --help                show help')
        print('-d, --decode [filepath]   decode file')
        print('-e, --encode [filepath]   encode file')

    elif (sys.argv[1] == '-v' or sys.argv[1] == '-v'):
        print('pnginator v1.0.0')

    else:
        print("Error: invalid argument")
