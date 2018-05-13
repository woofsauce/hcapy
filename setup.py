from setuptools import setup, find_packages, Extension
from Cython.Build import build_ext, cythonize


with open('README.md', encoding='utf-8') as f:
    readme = f.read()
with open('LICENSE') as f:
    li = f.read()

setup(
    name='hcapy',
    version='0.0.2',
    description='hca2wav wrapper working on Python3.',
    long_description=readme,
    author='Cryptomelone',
    author_email='cryptomelone@users.noreply.github.com',
    license=li,
    url='https://github.com/Cryptomelone/hcapy',
    packages=find_packages(exclude=('tests',)),
    ext_modules=[
        Extension("hcapy", sources=["module.pyx", "hca2wav/src/clHCA.cpp"], language="c++")
    ],
    cmdclass={'build_ext': build_ext},
)
