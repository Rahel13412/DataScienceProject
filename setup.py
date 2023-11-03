from setuptools import find_packages,setup



HYPEN_E_DOT = '-e .'

def get_requirements(filepath:str):
    '''this function will return a list of requirements'''
    requirements = []
    with open (filepath, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','')  for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements





setup(
    name ='mlproject',
    version='0.0.1',
    author='Rahel Ali',
    author_email='rahelali13412@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
