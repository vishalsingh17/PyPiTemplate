import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.3"

REPO_NAME = "PythonPackage"
AUTHOR_USERNAME = "VS17"
SRC_REPO = "PythonPackage"
AUTHOR_EMAIL = "vishal170997@gmail.com"
GITHUB_USERNAME = "vishalsingh17"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)