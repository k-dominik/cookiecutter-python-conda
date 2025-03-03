import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
package_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, package_name):
    print(f'ERROR: {package_name} is not a valid Python module name!')
    sys.exit(1)
