import re



def extract_title(contents):
    """
    """

    # Get all strings that start with TITLE
    title_string_regex = re.compile("^TITLE")
    title_strings  = list(filter(lambda c: re.search(title_string_regex, c),
                                 contents))

    # extract titles from them
    title_extract_regex = re.compile("\s+\d*(.*)-*")


    pdb_title = [re.search(title_extract_regex, title_string)
                 .group(1)
                 .strip() # remove whitespace
                 for title_string in title_strings]

    return "".join(pdb_title)


def extract_filename(contents):
    """
    """
    header_string_regex = re.compile("^HEADER")

    # Get all strings that start with HEADER
    header_strings  = filter(lambda string: re.match(header_string_regex, string),
                             contents)

    # TODO: what if no header strings?

    # extract filename
    file_name_regex = re.compile("\w+$")

    # Use only the first one
    first_header_string = next(header_strings)
    header = re.findall(file_name_regex,first_header_string)[0]
    return header


def parse_pdb(contents):
    """
    """
    print("Contents are: ")
    print(contents)
