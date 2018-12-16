"""Clean-up, remove optional unused stuff"""
import os


def remove_black():
    os.remove(".pre-commit")


def remove_ci():
    os.remove(".travis.yml")


def remove_versioning():
    os.remove(".bumpversion.cfg")


def main():
    print('removing unnecessary files...')
    if "{{ cookiecutter.use_black }}".lower() == 'n':
        remove_black()
    if "{{ cookiecutter.use_ci }}".lower() == 'n':
        remove_ci()
    if "{{ cookiecutter.use_bumpversion }}".lower() == 'n':
        remove_versioning()

    print("project initialized!")


if __name__ == '__main__':
    main()
