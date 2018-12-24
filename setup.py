import setuptools
import os
with open("README.md", "r") as fh:
    long_description = fh.read()
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setuptools.setup(
     name='fcs',  
     version='0.2',
     scripts=['fcs_pkg/fcs'],
     author="Ammar Alyousfi",
     author_email="ammar5656@gmail.com",
     description="A simple, powerful, and open-source time tracker from the command line",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
    #  packages=["fcs_pkg"],
    #  package_dir={'fcs_pkg': 'fcs_pkg'},
     package_data={'': ['*.mp3']},
     install_requires=install_requires,
    #  data_files=[('', ['rings/1.mp3'])],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )