from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='shadowdice',
    version='0.1.0',
    description='A tabletop role-playing gaming dice rolling library',
    long_description=readme,
    author='Shih Huan Chien',
    author_email='shc261392@gmail.com',
    url='https://github.com/shc261392/shadowdice',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
