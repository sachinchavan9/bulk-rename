from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name = 'bulk-rename',
    version = '2.0.6',
    author = 'Sachin Chavan',
    author_email = 'sachinewx@gmail.com',
    packages = ['bulk-rename'],
    scripts = ['bin/bulk-rename'],
    url = 'https://github.com/sachinchavan9/bulk-rename.git',
    license = 'GNU General Public License v2.0',
    description = 'Bulk file rename tool',
    long_description = long_description,
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
