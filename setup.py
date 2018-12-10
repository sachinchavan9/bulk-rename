from setuptools import setup

setup(
    name = 'bulk-rename',
    version = '1.0.0',
    author = 'Sachin Chavan',
    author_email = 'sachinewx@gmail.com',
    packages = ['bulk-rename'],
    scripts = ['bin/bulk-rename'],
    url = 'https://github.com/sachinchavan9/bulk-rename.git',
    license = open("LICENSE.md").read(),
    description = 'Bulk file rename tool',
    long_description = open("README.md").read(),
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Users',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Tool',
    ],
)
