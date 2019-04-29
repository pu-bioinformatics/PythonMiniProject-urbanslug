import amino.amino.parser as parser


class TestParser:
    pdb = [
        "HEADER    HYDROLASE/HYDROLASE INHIBITOR           17-MAY-11   3AYU          ",
        "TITLE     CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH APP-",
        "TITLE    2 DRIVED DECAPEPTIDE INHIBITOR",
        'SEQRES   1 A  167  TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN          ',
        'SEQRES   2 A  167  GLN ILE THR TYR ARG ILE ILE GLY TYR THR PRO ASP LEU          ',
        'SEQRES   3 A  167  ASP PRO GLU THR VAL ASP ASP ALA PHE ALA ARG ALA PHE          ',
        'SEQRES   4 A  167  GLN VAL TRP SER ASP VAL THR PRO LEU ARG PHE SER ARG          ',
        'SEQRES   5 A  167  ILE HIS ASP GLY GLU ALA ASP ILE MET ILE ASN PHE GLY          ',
        'SEQRES   6 A  167  ARG TRP GLU HIS GLY ASP GLY TYR PRO PHE ASP GLY LYS          ',
        'SEQRES   7 A  167  ASP GLY LEU LEU ALA HIS ALA PHE ALA PRO GLY THR GLY          ',
        'SEQRES   8 A  167  VAL GLY GLY ASP SER HIS PHE ASP ASP ASP GLU LEU TRP          ',
        'SEQRES   9 A  167  THR LEU GLY LYS GLY VAL GLY TYR SER LEU PHE LEU VAL          ',
        'SEQRES  10 A  167  ALA ALA HIS ALA PHE GLY HIS ALA MET GLY LEU GLU HIS          ',
        'SEQRES  11 A  167  SER GLN ASP PRO GLY ALA LEU MET ALA PRO ILE TYR THR          ',
        'SEQRES  12 A  167  TYR THR LYS ASN PHE ARG LEU SER GLN ASP ASP ILE LYS          ',
        'SEQRES  13 A  167  GLY ILE GLN GLU LEU TYR GLY ALA SER PRO ASP                  ',
        'SEQRES   1 B   10  ILE SER TYR GLY ASN ASP ALA LEU MET PRO',
        'HELIX    1   1 ASP A   27  ASP A   44  1                                  18    ',
        'HELIX    2   2 LEU A  114  MET A  126  1                                  13    ',
        'HELIX    3   3 SER A  151  GLY A  163  1                                  13    ',
        'SHEET    1   A 2 ASN A   2  PHE A   3  0                                        ',
        'SHEET    2   A 2 LEU A 128  GLU A 129 -1  O  GLU A 129   N  ASN A   2           ',
        'SHEET    1   B 6 ARG A  49  ARG A  52  0                                        ',
        'SHEET    2   B 6 GLN A  14  ILE A  19  1  N  ILE A  15   O  ARG A  49           ',
        'SHEET    3   B 6 ILE A  60  GLY A  65  1  O  ILE A  62   N  ARG A  18           ',
        'SHEET    4   B 6 SER A  96  ASP A  99  1  O  PHE A  98   N  GLY A  65           ',
        'SHEET    5   B 6 ALA A  83  PHE A  86 -1  N  HIS A  84   O  HIS A  97           ',
        'SHEET    6   B 6 ALA B   7  LEU B   8  1  O  LEU B   8   N  ALA A  85           ',
        'SHEET    1   C 2 TRP A 104  THR A 105  0                                        ',
        'SHEET    2   C 2 TYR A 112  SER A 113  1  O  TYR A 112   N  THR A 105',
    ]

    # TODO: DRY this example
    a_chain = 'B  10  TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'
    a_chain_aa = 'TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'
    another_chain = 'A  167  TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'
    another_chain_aa = 'TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'

    first_seq = 'TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN GLN ILE THR TYR \
ARG ILE ILE GLY TYR THR PRO ASP LEU ASP PRO GLU THR VAL ASP ASP ALA PHE ALA \
ARG ALA PHE GLN VAL TRP SER ASP VAL THR PRO LEU ARG PHE SER ARG ILE HIS \
ASP GLY GLU ALA ASP ILE MET ILE ASN PHE GLY ARG TRP GLU HIS GLY ASP GLY \
TYR PRO PHE ASP GLY LYS ASP GLY LEU LEU ALA HIS ALA PHE ALA PRO GLY THR \
GLY VAL GLY GLY ASP SER HIS PHE ASP ASP ASP GLU LEU TRP THR LEU GLY LYS \
GLY VAL GLY TYR SER LEU PHE LEU VAL ALA ALA HIS ALA PHE GLY HIS ALA MET \
GLY LEU GLU HIS SER GLN ASP PRO GLY ALA LEU MET ALA PRO ILE TYR THR \
TYR THR LYS ASN PHE ARG LEU SER GLN ASP ASP ILE LYS GLY ILE GLN GLU LEU TYR GLY ALA SER PRO ASP'

    second_seq = 'ILE SER TYR GLY ASN ASP ALA LEU MET PRO'

    def test_isolate_with_header(self):
        assert next(parser.isolate_with_header(
            '^HEADER', TestParser.pdb)) == TestParser.pdb[0]
        assert list(parser.isolate_with_header(
            '^TITLE', TestParser.pdb)) == TestParser.pdb[1:3]
        assert list(parser.isolate_with_header(
            '^SEQRES', TestParser.pdb)) == TestParser.pdb[3:17]
        assert list(parser.isolate_with_header(
            '^HELIX', TestParser.pdb)) == TestParser.pdb[17:20]
        assert list(parser.isolate_with_header(
            '^SHEET', TestParser.pdb)) == TestParser.pdb[20:30]

    def test_title_extraction(self):
        expected_title = "CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH \
APP-DRIVED DECAPEPTIDE INHIBITOR"

        title_strings = parser.isolate_with_header('^TITLE', TestParser.pdb)
        assert parser.extract_title(title_strings) == expected_title

    def test_extract_filename(self):
        header_string = parser.isolate_with_header('^HEADER', TestParser.pdb)
        assert parser.extract_filename(header_string) == "3AYU"

    def test_chain_set(self):
        raw_chains = parser.isolate_with_header('^SEQRES', TestParser.pdb)
        # removes header and number from chains
        mixed_chains = parser.extract_mixed_chains(raw_chains)
        assert parser.chain_set(mixed_chains) == {'A', 'B'}

    def test_split_chains(self):
        raw_chains = parser.isolate_with_header('^SEQRES', TestParser.pdb)
        # removes header and number from chains
        mixed_chains = parser.extract_mixed_chains(raw_chains)

        first_chain = mixed_chains[0:13]
        second_chain = [mixed_chains[13]]

        assert parser.split_chains(
            TestParser.pdb) == [first_chain, second_chain]

    def test_isolate_amino_acids(self):
        # Given a chain extract the AA in them
        assert parser.extract_amino_acids(
            TestParser.a_chain) == TestParser.a_chain_aa
        assert parser.extract_amino_acids(
            TestParser.another_chain) == TestParser.another_chain_aa

    def test_generate_full_chain(self):
        [first_chain, second_chain] = parser.split_chains(TestParser.pdb)
        first_seq = 'TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN GLN ILE THR TYR \
ARG ILE ILE GLY TYR THR PRO ASP LEU ASP PRO GLU THR VAL ASP ASP ALA PHE ALA \
ARG ALA PHE GLN VAL TRP SER ASP VAL THR PRO LEU ARG PHE SER ARG ILE HIS \
ASP GLY GLU ALA ASP ILE MET ILE ASN PHE GLY ARG TRP GLU HIS GLY ASP GLY \
TYR PRO PHE ASP GLY LYS ASP GLY LEU LEU ALA HIS ALA PHE ALA PRO GLY THR \
GLY VAL GLY GLY ASP SER HIS PHE ASP ASP ASP GLU LEU TRP THR LEU GLY LYS \
GLY VAL GLY TYR SER LEU PHE LEU VAL ALA ALA HIS ALA PHE GLY HIS ALA MET \
GLY LEU GLU HIS SER GLN ASP PRO GLY ALA LEU MET ALA PRO ILE TYR THR \
TYR THR LYS ASN PHE ARG LEU SER GLN ASP ASP ILE LYS GLY ILE GLN GLU LEU TYR GLY ALA SER PRO ASP'

        second_seq = 'ILE SER TYR GLY ASN ASP ALA LEU MET PRO'

        assert parser.generate_full_chain(first_chain) == first_seq
        assert parser.generate_full_chain(second_chain) == second_seq

    def test_count_amino_acids(self):
        [first_chain, second_chain] = parser.split_chains(TestParser.pdb)
        assert parser.count_amino_acids(first_chain) == 167
        assert parser.count_amino_acids(second_chain) == 10

    def test_generate_aa_sequence(self):
        p = 'YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRF\
SRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDD\
DELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRL\
SQDDIKGIQELYGASPD'

        b = 'ISYGNDALMP'
        assert parser.generate_aa_sequence(TestParser.first_seq) == p
        assert parser.generate_aa_sequence(TestParser.second_seq) == b

    def test_number_of_sheets_for_each_chain(self):
        assert parser.sheets_per_chain(TestParser.pdb) == {'A': 9, 'B': 1}

    def test_number_of_helices_for_each_chain(self):
        assert parser.helices_per_chain(TestParser.pdb) == {'A': 3, 'B': 0}

    def test_extract_all_aa(self):
        raw_chains = parser.isolate_with_header('^SEQRES', TestParser.pdb)
        # removes header and number from chains
        mixed_chains = parser.extract_mixed_chains(raw_chains)

        all_aa = mixed_chains[0:13] + [mixed_chains[13]]

        assert parser.extract_all_aa(
            TestParser.pdb) == parser.generate_full_chain(all_aa)

    def test_count_each_aa(self):
        aa_seq = parser.extract_all_aa(TestParser.pdb)
        aa_count = parser.count_each_aa(aa_seq)
        assert aa_count['ALA'] == 15
