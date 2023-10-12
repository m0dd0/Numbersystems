import setuptools

setuptools.setup(
    name="numbersystems",
    version="0.0.1",
    author="Moritz Hesche",
    author_email="it@ewb-karlsruhe.de",
    # description="",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="",
    classifiers=["Programming Language :: Python :: 3"],
    packages=setuptools.find_packages(),
    python_requires="~=3.10",
    install_requires=[],
    extras_require={"dev": ["black", "pylint", "jupyter", "ipykernel"]},
    include_package_data=True,
)
