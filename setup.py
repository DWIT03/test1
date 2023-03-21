from setuptools import setup, find_packages

setup(
    name='pyvncs',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'Pillow',
    ],
    url='https://github.com/radixcl/pyvncs',
    license='MIT',
    author='radixcl',
    description='Python VNC server and client'
)
