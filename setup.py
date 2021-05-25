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
      long_description="## TODO\r\n\r\n\r\nAdded a suggested template for the final screen to the 'main' file.\r\n\r\nS2 TASKS DUE BY 11TH MAY\r\n\r\n- Update the PSD (law students only)\r\n- Disable debug\r\n- Add authors to metadata\r\n- (COMPLETED) Interview title set to descriptive name\r\n- update read me (see below)\r\n- (COMPLETED) Flinders attribution\r\n- Default values (I dont think this applies for our app)\r\n- push to 'final' branch\r\n\r\nFeedback from S1\r\n\r\n- (COMPLETED) Make URL for website clickable, make email/phone numbers clickable\r\n- (COMPLETED) Avoid gross line break in printout, tell word to not paginate\r\n- (COMPLETED) Repeat row headers on each new page\r\n- (IN PROGRESS) Make dark purple bar update when reviewing questions (consistent and clear)\r\n- (COMPLETED KINDA) Make purple bar update roughly to position of navigation button (added percentage)\r\n- (CANT DO) Possibly make bar have sections (not sure how)\r\n- (IN PROGRESS) Maybe remove the printout when there’s no results\r\n\r\n**Read Me Instructions**\r\n\r\nThe README.md file for your app should contain a short description of what your application does and why it was written.\r\nREADME.md is a Markdown file. Use appropriate Markdown tags to ensure your README.md is clear, easy to read and descriptive.\r\nYou may credit yourselves in the README.md if you wish (but this is not required)\r\n\r\nFamily Law Directory\r\n\r\nCreated by Jessica Moncrieff, Michael Doroch, Ebony Algate, and Nathaniel Ramesh\r\nOrganisation: Flinders University\r\n\r\nThis application was created to assist couples, who are separating, in comparing and finding a family lawyer. The application will ask the user what region they are located in, and whether they require a lawyer who speaks another language. The application will then provide the user with a list of family lawyers matching their search criteria.\r\n\r\nThis application was created for, and in collaboration with,  the Family Law Pathways Network (SA), a  subsidiary of Relationships Australia (SA). Relationships Australia (SA) is a public company and not-for-profit organisation dedicated to providing Vulnerable Australians with Access to services. ABN: 19 119 188 500.",
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

