from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="svalint",
    version="2.4.3",  
    packages=find_packages(where="src"),  
    package_dir={"": "src"},  
    python_requires=">=3.8",  
    description="SVA Linter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AsFigo",
    author_email="support@asfigo.com",
    install_requires=[
        "tomli",
        "anytree",
        "python-string-utils",
    ],
    url="https://github.com/prajapati93/afsvalint",
    entry_points={
        "console_scripts": [
            "svalint=afsvalint.cli:main",  # maps `svalint` command
        ],
    },
)
