from setuptools import find_packages, setup

setup(
    name="Lab02-IA",
    author ="Gabriela Contreras",
    python_requires=">=3.6",
    long_description = open("README.md").read(),
    long_description_content_type ="text/markdown",
    entry_points={"console_scripts":["Lab02-IA=Lab02-IA.cli:main"]},
    requires=["BayesianNetwork","TabularCPD","VariableElimination"],
    
    packages= find_packages(where="src"),
    package_dir={"":"src/","Lab02-IA":"src/Lab02-IA"},
    url="https://github.com/dele20361/Lab02-IA",
    version="1.0.0",
    
)


