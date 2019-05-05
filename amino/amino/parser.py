import re, operator, itertools

IUPAC_AA_codes = {
    'CYS': 'C',
    'ASP': 'D',
    'SER': 'S',
    'GLN': 'Q',
    'LYS': 'K',
    'ILE': 'I',
    'PRO': 'P',
    'THR': 'T',
    'PHE': 'F',
    'ASN': 'N',
    'GLY': 'G',
    'HIS': 'H',
    'LEU': 'L',
    'ARG': 'R',
    'TRP': 'W',
    'ALA': 'A',
    'VAL': 'V',
    'GLU': 'E',
    'TYR': 'Y',
    'MET': 'M'
}

sec_structure = {
    'helix': '/',
    'sheet': '|',
}


def isolate_with_header(regex_string, contents):
    title_string_regex = re.compile(regex_string)
    title_strings = filter(lambda c: re.search(title_string_regex, c),
                           contents)
    return title_strings


#TODO: remove
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


#TODO: remove
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


def chain_set(mixed_chains):
    """
    Gives you a set of all the chains contained in the PDB file
    """
    return set([i[0] for i in mixed_chains])


def extract_all_chains(seq_section_gen):
    """
    Take the SEQRES section of the PDB file and return a dict of chain to aa
    """
    raw_chains = list(seq_section_gen)

    chain_isolation_regex = re.compile(r'^\w+\s+\d+\s+(.*)')

    mixed_chains = [
        re.search(chain_isolation_regex,
                  raw_chain).group(1).strip()  # remove whitespace
        for raw_chain in raw_chains
    ]

    mixed_chains = extract_mixed_chains(raw_chains)

    x = re.compile(r'^\w+\s+\d+\s+(.*)')

    # Create a dict of empty lists
    init = dict((chain, '') for chain in chain_set(mixed_chains))

    [
        init.update(
            {i[0]: init[i[0]] + ' ' + re.search(x, i).group(1).strip()})
        for i in mixed_chains
    ]

    return init


def extract_all_aa(contents):
    """
    Extract the entire aa sequence in a file
    Takes the dict from all_chains and merges the values
    """
    # TODO: Take the dict from extract_all_chains and merges the values
    aa_chains = split_chains(contents)
    y = list(itertools.chain(*aa_chains))
    return generate_full_chain(y)


def count_each_aa(aa_seq):
    """
    Count number of occurences of *each amino acid*
    Takes the entire aa sequence and returns a dictionary of {AA: int}
    """
    amino_acids = IUPAC_AA_codes.keys()
    return dict((aa, aa_seq.count(aa)) for aa in amino_acids)


# TODO: remove
def extract_amino_acids(chain):
    aa_isolation_regex = re.compile(r'^\w+\s+\d+\s+(.*)')
    return re.search(aa_isolation_regex, chain).group(1).strip()


# TODO: remove
def generate_full_chain(chain):
    """
    Takes a chain as a list of strings. Returns a single string
    """
    list_of_subchains = [extract_amino_acids(subchain) for subchain in chain]
    # Join list into single string separated by spaces
    return ' '.join(list_of_subchains)


# TODO: update
def count_amino_acids(all_aa_chains):
    """
    Count the number of aa *per chain*
    Take a dict from entire aa sequence and return a dictionary of {chain: int}
    """

    # Count the spaces and add 1 to get number of amino acids
    return dict(
        (chain, all_aa_chains[chain].count(' ')) for chain in all_aa_chains)


def generate_aa_sequence(chain):
    """
    Generate an aa sequence from a sequence of three letter amino acid codes
    Expects to receive a single string of three letter codes
    """

    chain.strip()
    chain_list = chain.split(' ')
    # TODO: What if aa is not in the lookup
    seq = [IUPAC_AA_codes[aa] for aa in chain_list]
    return ''.join(seq)


def generate_aa_sequence_for_disp(aa_seq):
    """
    Take aa seq from generate_aa_sequence and insert a newline every 50 chars.
    """
    return re.sub("(.{50})", "\\1\n", aa_seq, 0, re.DOTALL)


# TODO: merge helices and chain
def sheets_per_chain(contents):
    """
    """
    sheets = list(isolate_with_header('^SHEET', contents))
    r = re.compile(r'[A-Z]\W[A-Z]')

    raw_chains = isolate_with_header('^SEQRES', contents)
    #set of chains
    mixed_chains = extract_mixed_chains(raw_chains)
    c = chain_set(mixed_chains)

    # string of ...
    j = [re.search(r, sheet)[0][2] for sheet in sheets]
    k = ''.join(j)

    return dict((chain, k.count(chain)) for chain in c)


def helices_per_chain(contents):
    """
    """
    helices = list(isolate_with_header('^HELIX', contents))

    raw_chains = isolate_with_header('^SEQRES', contents)
    #set of chains
    mixed_chains = extract_mixed_chains(raw_chains)
    c = chain_set(mixed_chains)

    r = re.compile(r'[A-Z]\W[A-Z]')

    # string of ...
    j = [re.search(r, sheet)[0][2] for sheet in helices]
    k = ''.join(j)

    return dict((chain, k.count(chain)) for chain in c)


def extract_title(title_strings_gen):
    """
    """
    title_strings = list(title_strings_gen)

    # extract titles from them
    title_extract_regex = re.compile(r'\s+\d*(.*)-*')

    pdb_title = [
        re.search(title_extract_regex,
                  title_string).group(1).strip()  # remove whitespace
        for title_string in title_strings
    ]

    return "".join(pdb_title)


def extract_filename(header_string):
    """
    Takes a generator/filter object and gets only the first element
    Ignores the likelihood of more than one HEADER line
    Extracts the last word from the line and assumes it to be the file name.
    """

    # Get the last word in the string
    file_name_regex = re.compile(r'\w+$')

    # Use only the first one
    first_header_string = next(header_string)
    header = re.findall(file_name_regex, first_header_string.strip())[0]
    return header
