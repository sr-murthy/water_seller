from setuptools import setup, find_packages


setup(
    name='water-seller',
    version='0.2.0',
    author='maxwell flitton',
    author_email='maxwellflitton@gmail.com',
    packages=find_packages(exclude=("tests",)),
    scripts=[],
    url="https://github.com/OasisLMF/camel",
    description='basic installation tool for OasisLMF',
    long_description="basic installation tool for OasisLMF",
    package_data={'': ['script.sh']},
    include_package_data=True,
    install_requires=[
        "gerund @ git+https://github.com/OasisLMF/gerund"
    ],
    entry_points={
        "console_scripts": [
            "ws-install-oasislmf=water_seller.install.oasislmf.entry_points.install:main"
        ]
    },
)
