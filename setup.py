from distutils.core import setup

setup(
    name='fstring2fst',
    version='0.1.0',
    author='Þorsteinn Daði Gunnarsson',
    author_email='thorsteinng@ru.is',
    scripts=['fstring2fst.py'],
    license='LICENSE.txt',
    description='Use fstrings to create a fst.',
    long_description=open('README.md').read(),
    install_requires=[
        "openfst-python==1.7.3",
    ],
)
