from setuptools import setup, find_packages


version = '1.1'


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
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords="zope zcml hook",
      author="Martin Aspeli",
      author_email="zope-dev@zope.org",
      url="https://github.com/zopefoundation/z3c.zcmlhook",
      license="ZPL",
      namespace_packages=["z3c"],
      packages=find_packages("src"),
      package_dir={"": "src"},
      include_package_data=True,
      zip_safe=False,
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
