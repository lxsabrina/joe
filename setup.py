import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="joe",  
    version="1.0", 
    author="joe", 
    author_email="zx_genius@126.com",
    description="toytools",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/lxsabrina/joe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Independent",
    ],
    install_requires=[
        "pillow"
    ],
    python_requires=">=3",
)
