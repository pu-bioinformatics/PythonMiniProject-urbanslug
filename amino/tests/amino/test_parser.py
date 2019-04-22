import amino.amino.parser as parser



class TestParser:
    pdb = ["HEADER    HYDROLASE/HYDROLASE INHIBITOR           17-MAY-11   3AYU",
           "TITLE     CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH APP-",
           "TITLE    2 DRIVED DECAPEPTIDE INHIBITOR"]

    def test_title_extraction(self):

        expected_title = "CRYSTAL STRUCTURE OF MMP-2 ACTIVE SITE MUTANT IN COMPLEX WITH \
APP-DRIVED DECAPEPTIDE INHIBITOR"


        assert parser.extract_title(TestParser.pdb) == expected_title

    def test_filename_extraction(self):
        assert parser.extract_filename(TestParser.pdb) == "3AYU"

    def test_chain_extraction(self):
        pass

