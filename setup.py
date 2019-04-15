from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "Amino",
    version = "0.0.0.1",
    description = "A collection of modules for performing simple PDB file analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = "Njagi Mwaniki",
    author_email= "njagi@urbanslug.com",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=find_packages(),
    test_suite="pdb.tests"
)
