from os import listdir
from os.path import join, isdir


def search(directory, filename):
    dirs = [directory]
    print(dirs)
    while dirs:
        current = dirs.pop(0)
        print(current)
        print(listdir(current))
        for subPath in listdir(current):
            if subPath == filename:
                return True
            path = join(current, subPath)
            if isdir(path):
                dirs.append(path)
    return False


print(search('E:/', 'cz.txt'))
