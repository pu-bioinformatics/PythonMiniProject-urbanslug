import re, operator, itertools


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


def extract_amino_acids(chain):
    aa_isolation_regex = re.compile(r'^\w+\s+\d+\s+(.*)')
    return re.search(aa_isolation_regex, chain).group(1).strip()


def count_amino_acids(chain):
    """
    Generate an aa sequence from a chain
    Expects to receive a single chain as a list
    """
    pass


def generate_aa_sequence(chain):
    """
    Generate an aa sequence from a chain
    Expects to receive a single chain as a list
    """
    pass


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
