from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:
    '''This function reads the requirements file 
    and returns a list of requirements'''
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # .strip() is neater than replace
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='cellvoltage',
    version='0.0.1',
    author='John Mike',
    author_email='jmasamvu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
