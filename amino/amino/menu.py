import amino.amino.pdb as pdb
import amino.amino.parser as parser



loaded = "None"
contents = None

def option_handler(option):
    global contents, loaded
    opt = str.lower(option)

    # TODO: figure out why opt doesn't update
    while opt != 'q':
        if opt == "o":
            loaded = input("Enter a valid path for a PDB File: ")
            contents = pdb.pdb_handler(loaded)
        elif opt == "i":
            parser.parse_pdb(contents)
        elif opt == "h":
            pass
        elif opt == "s":
            pass
        elif opt == "x":
            pass
        else:
            print ("%s is not a valid option.\n\n" % option)
        start()

    if opt == "q":
        print("PDB analyzer exiting")

def reloader():
    global loaded
    if not loaded:
        p = input("Are you sure you want to replace the loaded file (y|N): " )
        if p:
            pass
        else:
            pass


def overall_menu():
    global loaded

    print(
        """
********************************************************************************
* PDB FILE ANALYZER                                                            *
********************************************************************************
* Select an option from below:                                                 *
*                                                                              *
* 1) Open a PDB File                  (O)                                      *
* 2) Information                      (I)                                      *
* 3) Show histogram of amino acids    (H)                                      *
* 4) Display Secondary Structure      (S)                                      *
* 5) Export PDB File                  (X)                                      *
* 6) Exit                             (Q)                                      *
*                                                                              *
*                                                   Current PDB: %s *
********************************************************************************
    """ % loaded)
    option = input(": ")
    return option

def file_loader():
    path = input("Enter a valid path for a PDB file: ")
    return path

def start():
    opt = overall_menu()
    option_handler(opt)
