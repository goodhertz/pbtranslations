import setuptools

long_description = """
### PB
"""

setuptools.setup(
    name="pbt",
    version="0.0.1",
    author="Goodhertz, Inc.",
    author_email="rob@goodhertz.com",
    description="Audio plugin translations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goodhertz/pbtranslations",
    packages=[
        "pbt"
    ],
    install_requires=[
        "coldtype>=0.1.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
