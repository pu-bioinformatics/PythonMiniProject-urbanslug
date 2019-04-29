import amino.amino.parser as parser


def gen_title_str(title):
    return 'Title: ' + title


def gen_filename_str(filename):
    return "PDB File: " + filename + ".pdb"


def summary(contents):
    """
    output summary info
    """

    header_string = parser.isolate_with_header('^HEADER', contents)
    title_string = parser.isolate_with_header('^TITLE', contents)
    seq_res = parser.isolate_with_header('^SEQRES', contents)

    # Filename
    filename = parser.extract_filename(header_string)
    print(gen_filename_str(filename))

    # Title
    title = parser.extract_title(title_string)
    print(gen_title_str(title))

    # Chain

    # Pad with newlines
    print('\n\n')


def histogram():
    pass


def sec_structure():
    pass
