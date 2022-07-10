from setuptools import setup

setup(
    name='sfst',
    version='0.1.0',
    description='A Python package for Nondeterministic Finite Automata',
    url='https://github.com/soroushfathi/NFST_Python',
    author='Soroush Fathi',
    author_email='soroush8fathi@gmail.com',
    license='BSD 2-clause',
    packages=['sfst'],
    install_requires=['mpi4py>=2.0', ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
