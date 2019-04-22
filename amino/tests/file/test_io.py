import os
import pytest

import amino.file.io as io


class TestPdbLoading:
    def test_loader(self):

        if not os.path.isdir('./data/tests'):
            os.mkdir('./data/tests')

        file_path = "./data/tests/my_file.pdb"
        non_existent_file_path = "./data/tests/no_file.pdb"
        contents = "We are"

        my_file = open(file_path, 'w')
        my_file.writelines(contents)
        my_file.close()

        # loads existing files
        assert io.loader(file_path) == contents

        # throws exception when pdb file isn't availanle
        with pytest.raises(FileNotFoundError):
            io.loader(non_existent_file_path)
