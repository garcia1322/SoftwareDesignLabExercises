from os import listdir
from os. path import isfile, join

def find(path, filename):
    for f in listdir(path):
        if isfile(join(path, f)):
            if filename in f:
                print(f)
    else:
        find(join(path, f), filename)

#put the path and filename here
find(r"C:/Users/User/PycharmProjects/zxcpoiqwe","GARCIA, MARKLAWRENCE_LABREPORT.docx")