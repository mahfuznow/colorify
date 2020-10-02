import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorify",
    version="1.0.2",
    author="Md. Mahfuzur Rahman",
    author_email="contact@mahfuznow.com",
    description="Bring life into your project by adding wonderful colors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahfuznow/colorify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
