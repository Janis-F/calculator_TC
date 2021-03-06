import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calculator',
    version='0.0.1',
    author='Janis Freimanis',
    author_email='janis.freimanis@hey.com',
    description='Simple calculator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Janis-F/calculator_TC.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
