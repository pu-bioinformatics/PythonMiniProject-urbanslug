from amino.file.io import loader


def load_pdb(path):
    try:
        contents = loader(path)
        print("The file %s has been successfully loaded." % path)
        return contents
    except FileNotFoundError:
        print("%s is not a valid file." % path)


def pdb_handler(path):
    contents = load_pdb(path)
    return contents
