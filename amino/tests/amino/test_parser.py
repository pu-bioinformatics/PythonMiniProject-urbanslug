import amino.amino.parser as parser


class TestParser:
    pdb = [
        "HEADER    HYDROLASE/HYDROLASE INHIBITOR           17-MAY-11   3AYU",
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
    ]

    def test_isolate_with_header(self):
        assert next(parser.isolate_with_header('^HEADER', TestParser.pdb)) == TestParser.pdb[0]
        assert list(parser.isolate_with_header('^TITLE', TestParser.pdb)) == TestParser.pdb[1:3]
        assert list(parser.isolate_with_header('^SEQRES', TestParser.pdb)) == TestParser.pdb[3:]


    def test_title_extraction(self):

        expected_title = "CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH \
APP-DRIVED DECAPEPTIDE INHIBITOR"

        assert parser.extract_title(TestParser.pdb) == expected_title

    def test_filename_extraction(self):
        assert parser.extract_filename(TestParser.pdb) == "3AYU"



    def test_chains(self):
        raw_chains = parser.isolate_with_header('^SEQRES', TestParser.pdb)
        # removes header and number from chains
        mixed_chains = parser.extract_mixed_chains(raw_chains)
        assert parser.chains(mixed_chains) == {'A', 'B'}



    def test_split_chains(self):
        raw_chains = parser.isolate_with_header('^SEQRES', TestParser.pdb)
        # removes header and number from chains
        mixed_chains = parser.extract_mixed_chains(raw_chains)

        first_chain = mixed_chains[0:13]
        second_chain = [mixed_chains[13]]

        assert parser.split_chains(TestParser.pdb) == [first_chain, second_chain]

    def test_isolate_amino_acids(self):
        # Given a chain extract the AA in them
        # TODO: DRY this test
        a_chain = 'B  10  TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'
        a_chain_aa = 'TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'
        another_chain = 'A  167  TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'
        another_chain_aa = 'TYR ASN PHE PHE PRO ARG LYS PRO LYS TRP ASP LYS ASN'

        assert parser.extract_amino_acids(a_chain) == a_chain_aa
        assert parser.extract_amino_acids(another_chain) == another_chain_aa


    def test_count_amino_acids(self):
        pass


    def test_generate_aa_sequence(self):

        [first_chain, second_chain] = parser.split_chains(TestParser.pdb)

        first_seq = 'YNFFPRKPKWDKNQITYRIIGYTPDLDPETVDDAFARAFQVWSDVTPLRF\
SRIHDGEADIMINFGRWEHGDGYPFDGKDGLLAHAFAPGTGVGGDSHFDD\
DELWTLGKGVGYSLFLVAAHAFGHAMGLEHSQDPGALMAPIYTYTKNFRL\
SQDDIKGIQELYGASPD'
        second_seq = 'ISYGNDALMP'

        assert parser.generate_aa_sequence(first_chain) == first_seq
        assert parser.generate_aa_sequence(second_chain) == second_seq
