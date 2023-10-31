from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'  # to create constant '-e .' to ignore this because it is not install & it is not a pakage

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:  # Open the file
        requirements = file_obj.readlines()  # Read each line in the file
        requirements = [req.replace("\n","") for req in requirements] # When file read there is "\n" in the list because of the new line to replace this "\n"

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
    

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Saroj Ghosh',
    author_email='sarojghoshdk@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)