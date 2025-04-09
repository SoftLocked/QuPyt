from setuptools import setup, find_packages

setup(
    name="QuPyt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy>=2.2.0'],
    author="Harikrishna Vardhineedi",
    author_email="harivardhineedi@gmail.com",
    description="Package to emulate and visualize quantum computations with a classical computer.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SoftLocked/QuPyt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.10',
)