import amino.amino.parser as parser


def gen_title_str(title):
    return 'Title: ' + title


def gen_filename_str(filename):
    return "PDB File: " + filename + ".pdb"


def display_chain(chain, count, helices, sheets, seq):
    """
    Display a chain along the lines of:
    - Chain A
      Number of amino acids: 167
      Number of helix:       3
      Number of sheet:       9
      Sequence: YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRF
                SRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDD
                DELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRL
                SQDDIKGIQELYGASPD
    """
    print("""
    - Chain %s
      Number of amino acids: %d
      Number of helix:       %d
      Number of sheet:       %d
    """ % (chain, count, helices, sheets))

    # TODO: pad with spaces
    print("""
      Sequence %s
    """ % seq)


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

    # Chains
    chains = parser.extract_all_chains(seq_res)  # a dict of chain to aa
    chains_uniq = list(chains.keys())
    chains_uniq.sort()

    she = parser.sheets_per_chain(contents)
    hel = parser.helices_per_chain(contents)

    aa_count = parser.count_amino_acids(chains)

    for chain in chains_uniq:
        helices = hel[chain]
        sheets = she[chain]

        seq = parser.generate_aa_sequence(chains[chain].strip())
        disp_seq = parser.generate_aa_sequence_for_disp(seq)
        count = aa_count[chain]

        display_chain(chain, count, helices, sheets, disp_seq)

    # Pad with newlines
    print('\n\n')


def histogram():
    pass


def sec_structure():
    pass
