import amino.amino.pdb as pdb
import amino.amino.output as output

global contents, loaded, keep_running

keep_running = True
loaded = "None"
contents = None


def exit_menu():
    """
    """
    global keep_running
    h = input("Really exit [y|N]: ")
    if str.lower(h) == 'y':
        s = input("Save before exiting [Y|n]: ")
        print("PDB analyzer exiting")
        keep_running = False
    else:
        start()


def load_file_menu():
    """
    """
    global contents
    loaded = input("Enter a valid path for a PDB File: ")
    contents = pdb.pdb_handler(loaded)


def option_handler(option):
    """
    """
    global contents
    opt = str.lower(option)

    # TODO: figure out why opt doesn't update
    if opt == "o":
        load_file_menu()
    elif opt == "i":
        output.summary(contents)
    elif opt == "h":
        pass
    elif opt == "s":
        pass
    elif opt == "x":
        pass
    elif opt == "q":
        exit_menu()
    else:
        print("%s is not a valid option.\n\n" % option)


def reloader():
    """
    """
    if not loaded:
        p = input("Are you sure you want to replace the loaded file (y|N): ")
        if p:
            pass
        else:
            pass


def print_overall_menu():
    """
    """
    print("""
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


def start():
    """
    """
    opt = print_overall_menu()
    option_handler(opt)

    if keep_running:
        start()
