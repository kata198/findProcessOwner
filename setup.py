#!/usr/bin/env python

from setuptools import setup



if __name__ == '__main__':

    summary = 'Application which scans a list of given pids and determines the executing user'
    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except Exception as e:
        sys.stderr.write('Exception reading long description: %s\n' %(str(e),))
        long_description = summary

    setup(name='findProcessOwner',
            version='1.0.1',
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            scripts=['findProcessOwner'],
            install_requires=['ProcessMappingScanner>1.0'],
            url='https://github.com/kata198/findProcessOwner',
            maintainer_email='kata198@gmail.com',
            description=summary,
            long_description=long_description,
            license='LGPLv3',
            keywords=['find', 'process', 'owner', 'unix', 'linux', 'pid', 'execute', 'running', 'username', 'uid'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
            ]
    )



