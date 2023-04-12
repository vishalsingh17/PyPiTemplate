import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "IPYNBrenderer"
AUTHOR_USERNAME = "VS17"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL = "vishal170997@gmail.com"
GITHUB_USERNAME = "vishalsingh17"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = "A python package",
    long_description_content = "text/markdown",
    url = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}",
    projects_urls = {
        "Bug Tracker": f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}/issues"
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)
