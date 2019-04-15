loaded = "None"

def option_handler(option):
    if option == "O":
        pdb_handler()
    elif option == "I":
        pass
    elif option == "H":
        pass
    elif option == "S":
        pass
    elif option == "X":
        pass
    elif option == "Q":
        pass
    else:
        print ("Not a valid option.\n\n")
        menu()

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
* 6)Exit                              (Q)                                      *
*                                                                              *
*                                                     Current PDB: %s *
********************************************************************************
    """ % loaded
    )
    option = input(": ")
    return option

def file_loader():
    path = input("Enter a Valid PATH for a PDB File: ")
    return path
