from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).parent


def find_requirements(filename):
    with open(ROOT / "requirements" / filename) as f:
        reqs = [line.strip() for line in f]
    return reqs


setup(
    name="geom",
    version="0.0.0",
    packages=find_packages(where="src", exclude=("test",)),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=find_requirements("requirements.txt"),
    extras_require={
        "dev": find_requirements("requirements-dev.txt"),
    },
)
