from setuptools import setup, find_packages


with open('README.md') as infile:
    long_description = infile.read()


### Kept as Example ###
# from setuptools.extension import Extension
# from Cython.Build import cythonize
# import numpy as np
# extensions = [
#     Extension(
#         "DeepVCF.cython_numpy.cython_np_array",
#         ["DeepVCF/cython_numpy/cython_np_array.pyx"],
#         include_dirs=[np.get_include()], # needed for cython numpy to_array
#         libraries=['',],
#         library_dirs=['', ], 
#     ),
# ]


setup(
    name='GenScript',
    version='0.0.1',  # major.minor.maintenance
    description='FARM stack (FastAPI, Retool, MongoDB) for the Protein Production Pipeline by connecting P4 to P3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tmsincomb/GenScript',
    author='Troy Sincomb',
    author_email='troysincomb@gmail.com',
    license='MIT',
    keywords='genscript',
    packages=find_packages('genscript'),
    # include_package_data=True,  # try this out: might be the reason packages didnt break since it wont run without this.
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 1 - ALPHA',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    #  TODO: add classifiers for machine learning/variant caller https://pypi.org/classifiers/
    install_requires=[
        'pandas',
        'pymongo',
    ],
    entry_points={
        'console_scripts': [
            'genscript=src.core:main',
        ],
    },
    ### Kept as Example ###
    # setup_requires=["cython"],
    # ext_modules=cythonize(extensions),  # used for initial build. 
    # ext_modules=extensions,  
)