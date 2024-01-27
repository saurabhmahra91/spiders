from setuptools import find_packages, setup


setup(
    name="spiderstore",
    version="0.0.1",
    description="Internet web scraper",
    package_dir={"": "spiderstore"},
    packages=find_packages(where="spiderstore"),
    url="https://github.com/saurabhmahra91/spiderstore.git",
    author="Saurabh Kumar Mahra",
    author_email="sourabhmahra91@gmail.com",
    license_files=("LICENSE.txt"),
    install_requires=[],
    extras_requires={
        "dev": ["twine>=4.0.2"]
    },
    python_requires=">=3.11",
)
