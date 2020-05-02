from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="parabot",
    version="1.0.0",
    description="Execute robotframework test files/tests in paralel, even without special preparation of them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bednaJedna/parabot",
    author="bednaJedna",
    author_email="bednarik.radek@gmail.com",
    packages=find_packages(),
    install_requires=["robotframework", "selenium", "robotframework-seleniumLibrary"],
    license="MIT",
    keywords="robotframework, parallel execution, test, testing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
