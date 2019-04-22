

def hist():
    """
    Show a histogram of amino acids
    """
    pass

def amino_menu():
    aa_menu_string = """
 Choose an option to order by:
 number of amino acids - ascending (an)
 number of amino acids - descending (dn)
 alphabetically - ascending (aa)
 alphabetically - descending (da)
    """

    print(aa_menu_string)
    order = input("order by: ")
