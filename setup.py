from setuptools import setup, find_packages

setup(
    name='gpt-to-chatgpt',
    version='0.1.0',
    description='Convert GPT Completion style message to a ChatGPT call',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package needs to run here
    ],
    entry_points={
        # If your package provides a command-line interface, define it here
    },
    classifiers=[
        # Add any classifiers that describe your package here, such as its supported Python versions
    ],
    author='Bram Adams',
    author_email='bram+support@bramadams.dev',
    url='https://github.com/bramses/gpt-to-chatgpt-py',
    license='MIT'
)