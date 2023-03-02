from setuptools import setup, find_packages
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='gpt-to-chatgpt',
    version='0.1.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Convert GPT Completion style message to a ChatGPT call',
    packages=find_packages(),
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=[
        # List any dependencies your package needs to run here
    ],
    entry_points={
        # If your package provides a command-line interface, define it here
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='Bram Adams',
    author_email='bram+support@bramadams.dev',
    url='https://github.com/bramses/gpt-to-chatgpt-py',
    license='MIT'
)