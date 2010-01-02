from setuptools import setup, find_packages
import os.path

version = '1.0b1'

setup(name                  = "z3c.zcmlhook",
      version               = version,
      description           = "Easily hook into the ZCML processing machinery",
      long_description      = open("README.txt").read() + "\n" +
                              open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers           = [
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Zope Public License",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords              = "zope zcml hook",
      author                = "Martin Aspeli",
      author_email          = "zope-dev@zope.org",
      url                   = "",
      license               = "ZPL",
      namespace_packages    = ["z3c"],
      packages              = find_packages("src", exclude=["ez_setup"]),
      package_dir           = {"": "src"},
      include_package_data  = True,
      zip_safe              = False,
      install_requires      = [
          "setuptools",
          "zope.component",
          "zope.interface",
          "zope.schema",
          "zope.configuration",
          ],
      extras_require        = {},
      tests_require         = "nose >=0.10.0b1",
      test_suite            = "nose.collector",
      )
