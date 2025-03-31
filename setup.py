from setuptools import find_packages
from setuptools import setup


version = '2.1'


def read(path):
    with open(path) as f:
        return f.read()


setup(name="z3c.zcmlhook",
      version=version,
      description="Easily hook into the ZCML processing machinery",
      long_description=(
          read("README.rst")
          + "\n"
          + read('CHANGES.rst')
      ),
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Zope Public License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
          "Programming Language :: Python :: 3.13",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords="zope zcml hook",
      author="Martin Aspeli",
      author_email="zope-dev@zope.dev",
      url="https://github.com/zopefoundation/z3c.zcmlhook",
      license="ZPL",
      namespace_packages=["z3c"],
      packages=find_packages("src"),
      package_dir={"": "src"},
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.9',
      install_requires=[
          "setuptools",
          "zope.component",
          "zope.interface",
          "zope.schema",
          "zope.configuration",
      ],
      extras_require=dict(
          test=[
              'zope.component[test]',
          ]),
      )
