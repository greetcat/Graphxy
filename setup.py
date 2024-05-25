from setuptools import setup, find_packages

setup(
    name='Graphxy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your dependencies here
    ],
    author='Gokul',
    author_email='gokul1357nms@gmail.com',
    description='A library for performing operations on graphs and trees',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/greetcat/Graphxy.git',  # Project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
