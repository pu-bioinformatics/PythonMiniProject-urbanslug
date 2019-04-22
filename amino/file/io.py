from os.path import isfile



def loader(path):
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

        return contents
    else:
        raise FileNotFoundError(path + " is not a valid file.")

