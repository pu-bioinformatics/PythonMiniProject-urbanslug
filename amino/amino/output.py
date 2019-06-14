import amino.amino.parser as parser
import collections


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


def histogram(contents, ordering):
    """
    Display histogram
    """
    aa_seq = parser.extract_all_aa(contents)
    aa_count = parser.count_each_aa(aa_seq)

    # {'CYS': 0, 'ASP': 20, 'SER': 8, 'GLN': 5, 'LYS': 7, 'ILE': 10, 'PRO': 11, 'THR': 8, 'PHE': 12, 'ASN': 5, 'GLY': 20, 'HIS': 7, 'LEU': 13, 'ARG': 7, 'TRP': 4, 'ALA': 15, 'VAL': 6, 'GLU': 6, 'TYR': 9, 'MET': 4}

    if ordering == 'an':  # no of aa ascending
        l = collections.OrderedDict(
            sorted(aa_count.items(), key=lambda t: t[1]))

    elif ordering == 'dn':  # no of aa descending
        l = collections.OrderedDict(
            sorted(aa_count.items(), key=lambda t: t[1], reverse=True))

    elif ordering == 'aa':  # alphabetically ascending
        l = collections.OrderedDict(
            sorted(aa_count.items(), key=lambda t: t[0]))
    elif ordering == 'da':  # alphabetically descending
        l = collections.OrderedDict(
            sorted(aa_count.items(), key=lambda t: t[0], reverse=True))

    for f in l:
        print("%s (%2d): " % (f, l[f]), end='')
        print('*' * l[f])


def print_chain(a, b, c):

    bb = parser.disp_sec_str(b)
    cc = parser.disp_sec_str(c)

    lines = bb.count('\n') + 1

    print("""
Chain %s:
(1)
    """ % a)

    # interleave them
    bb = bb.split('\n')
    cc = cc.split('\n')

    q = list(zip(bb, cc))

    for s in range(0, lines):
        for k in q[s]:
            print(k)

    return


def sec_structure(contents, filepath):
    """
    """
    header_string = parser.isolate_with_header('^HEADER', contents)
    filename = parser.extract_filename(header_string)

    seq_res = parser.isolate_with_header('^SEQRES', contents)

    print("Secondary Structure of the PDB id %s:" % filename)

    chains = parser.extract_all_chains(seq_res)
    chains_uniq = list(chains.keys())
    chains_uniq.sort()

    seqs = parser.secondary_structure(contents)

    for chain in chains_uniq:
        l = parser.generate_aa_sequence(chains[chain].strip())
        print_chain(chain, l, seqs[chain])


def export(filepath):
    print("Exporting nothing for now...")
