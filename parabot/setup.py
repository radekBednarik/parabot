from setuptools import setup, find_packages

setup(
    name="parabot",
    version="0.0.1",
    description="Execute robotframework test files/tests in paralel, even without special preparation of them",
    author="bednaJedna",
    packages=find_packages(),
    install_requires=["robotframework", "selenium", "robotframework-seleniumLibrary"],
    license="MIT",
    keywords="robotframework, parallel execution, test, testing",
)
