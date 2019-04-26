import re, operator, itertools


IUPAC_AA_codes = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                  'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
                  'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                  'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

def isolate_with_header(regex_string, contents):
    title_string_regex = re.compile(regex_string)
    title_strings = filter(lambda c: re.search(title_string_regex, c),
                           contents)
    return title_strings


def extract_mixed_chains(raw_chains):
    """
    Removed headers and numbers from chains
    """
    chain_isolation_regex = re.compile(r'^\w+\s+\d+\s+(.*)')

    mixed_chains = [
        re.search(chain_isolation_regex,
                  raw_chain).group(1).strip()  # remove whitespace
        for raw_chain in raw_chains
    ]
    return mixed_chains


def chains(mixed_chains):
    """
    Gives you a set of all the chains contained in the PDB file
    """
    return set([i[0] for i in mixed_chains])


def split_chains(contents):
    """
    Take many chains and spit them into multiple lists
    """
    raw_chains = list(isolate_with_header('^SEQRES', contents))
    mixed_chains = extract_mixed_chains(raw_chains)
    chains = [
        list(group)
        for _, group in itertools.groupby(mixed_chains,
                                          key=operator.itemgetter(0))
    ]

    return chains

def extract_all_aa(contents):
    """
    Get all amino acids in the file
    """
    aa_chains = split_chains(contents)
    y = list(itertools.chain(*aa_chains))
    return generate_full_chain(y)

def count_each_aa(aa_seq):
    amino_acids = IUPAC_AA_codes.keys()
    return dict((aa, aa_seq.count(aa)) for aa in amino_acids)

def extract_amino_acids(chain):
    aa_isolation_regex = re.compile(r'^\w+\s+\d+\s+(.*)')
    return re.search(aa_isolation_regex, chain).group(1).strip()

def generate_full_chain(chain):
    """
    Takes a chain as a list of strings. Returns a single string
    """
    list_of_subchains = [extract_amino_acids(subchain) for subchain in chain]
    # Join list into single string separated by spaces
    return ' '.join(list_of_subchains)


def count_amino_acids(chain):
    """
    Generate an aa sequence from a chain

    Expects to receive a single chain as a list
    A chain is a list of strings
    """
    full_chain = generate_full_chain(chain)
    # Count the spaces and add 1 to get number of amino acids
    return full_chain.count(' ') + 1

def generate_aa_sequence(chain):
    """
    Generate an aa sequence from a sequence of three letter amino acid codes
    Expects to receive a single string of three letter codes
    """


    chain_list = chain.split(' ')
    # TODO: What if aa is not in the lookup
    seq = [IUPAC_AA_codes[aa] for aa in chain_list]
    return ''.join(seq)

# TODO: merge helices and chain
def sheets_per_chain(contents):
    """
    """
    sheets = list(isolate_with_header('^SHEET', contents))
    r = re.compile(r'[A-Z]\W[A-Z]')

    raw_chains = isolate_with_header('^SEQRES', contents)
    #set of chains
    mixed_chains = extract_mixed_chains(raw_chains)
    c = chains(mixed_chains)

    

    # string of ...
    j = [re.search(r,sheet)[0][2] for sheet in sheets]
    k = ''.join(j)
    

    return dict((chain, k.count(chain)) for chain in c)


def helices_per_chain(contents):
    """
    """
    sheets = list(isolate_with_header('^HELIX', contents))
    r = re.compile(r'[A-Z]\W[A-Z]')

    raw_chains = isolate_with_header('^SEQRES', contents)
    #set of chains
    mixed_chains = extract_mixed_chains(raw_chains)
    c = chains(mixed_chains)

    

    # string of ...
    j = [re.search(r,sheet)[0][2] for sheet in sheets]
    k = ''.join(j)
    

    return dict((chain, k.count(chain)) for chain in c)


def extract_title(contents):
    """
    """

    # Get all strings that start with TITLE
    title_string_regex = re.compile("^TITLE")
    title_strings = list(
        filter(lambda c: re.search(title_string_regex, c), contents))

    # extract titles from them
    title_extract_regex = re.compile(r'\s+\d*(.*)-*')

    pdb_title = [
        re.search(title_extract_regex,
                  title_string).group(1).strip()  # remove whitespace
        for title_string in title_strings
    ]

    return "".join(pdb_title)


def extract_filename(contents):
    """
    """
    header_string_regex = re.compile("^HEADER")

    # Get all strings that start with HEADER
    header_strings = filter(
        lambda string: re.match(header_string_regex, string), contents)

    # TODO: what if no or multiple header strings?

    # extract filename
    file_name_regex = re.compile(r'\w+$')

    # Use only the first one
    first_header_string = next(header_strings)
    header = re.findall(file_name_regex, first_header_string)[0]
    return header


def parse_pdb(contents):
    """
    """
    print("Contents are: ")
    print(contents)
