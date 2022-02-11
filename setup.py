from setuptools import setup, find_packages

setup(
    name="pinter",
    version="0.0.1",
    url="https://github.com/flat35hd99/pinter.git",
    author="flat35hd99",
    author_email="flat35hd99@gmail.com",
    description="Pick up intersection of grouppair file of curp",
    packages=find_packages(),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["pinter=pinter.console:main"]},
)
