import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Scyscrapers_Severyn_Peleshko",
    version="0.0.1",
    author="Severyn Peleshko",
    author_email="s.peleshko@ucu.edu.ua",
    description="A package for checking if the game bord was built correct",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Severyn12/Task_one.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
