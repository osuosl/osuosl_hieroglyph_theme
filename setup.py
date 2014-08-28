from distutils.core import setup
from setuptools import setup

with open('README.rst', 'r') as f:
        long_description = f.read()

setup(
    zip_safe=False,
    install_requires=[
            "sphinx>=1.1",
            "hieroglyph>=0.6",
            ],
    name="osuosl_hieroglyph_theme",
    version=0.3,
    author="Lucy Wyman",
    author_email="lucyw@osuosl.org",
    description="Slides theme for  the OSU Open Source Lab",
    long_description=long_description,
    packages=['osuosl_hieroglyph_theme'],
    include_package_data=True,
    keywords="hieroglyph extension theme",
    url="https://github.com/osuosl/osuosl_hieroglyph_theme",
)

