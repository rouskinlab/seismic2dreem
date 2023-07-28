from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name="seismic2dreem",
    version='0.0.0',
    description="Converts seismic data to dreem format",
    long_description=readme,
    author="Yves Martin des Taillades for the Rouskin Lab",
    author_email="yves@martin.yt",
    url="https://github.com/rouskinlab/seismic2dreem",
    packages=find_packages(),
    install_requires=['pandas','numpy'],
    python_requires=">=3.9",
)
