from os.path import isfile

def func(x):
    return x + 4


def loader(file_path):
    """
    Takes a file path: checks that the file exists and reads it.
    Prints message explaining whether file has been loaded or not.

    Returns the loaded file.
    """

    if isfile(path):

        loaded = path

        pdb_file = open(path, 'r')
        contents = pdb_file.read()
        pdb_file.close()
        print("The file %s has been successfully loaded." % path)
        return contents
    else:
        print("%s is not a valid file." % path)

