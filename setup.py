import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S1FLPN2',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='## FAMILY LAW DIRECTORY\r\n\r\n***Created by*** *Jessica Moncrieff, Michael Doroch, Ebony Algate, and Nathaniel Ramesh*\r\n\r\n***Organisation:*** *Flinders University*\r\n\r\nThis application was created to assist separating couples in comparing and finding a family lawyer. The application will ask the user what region they are located in, and whether they require a lawyer who speaks another language. The application will then provide the user with a list of family lawyers matching their search criteria.\r\n\r\nThis application was created for, and in collaboration with,  the Family Law Pathways Network (SA), a  subsidiary of Relationships Australia (SA). Relationships Australia (SA) is a public company and not-for-profit organisation dedicated to providing Vulnerable Australians with Access to services. ABN: 19 119 188 500.\r\n',
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S1FLPN2/', package='docassemble.LLAW33012021S1FLPN2'),
     )

