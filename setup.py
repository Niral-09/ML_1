from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_req(file_path:str)->List[str]:
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [re.replace("\n", "") for re in req]
        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    pass

setup(
    name="ML_project",
    version="0.0.1",
    author="Niral Patel",
    author_email="niral0901@gmail.com",
    packages=find_packages(),
    install_requires=get_req('C:\\Users\\91878\\Desktop\\ML_project\\requirements.txt')
)