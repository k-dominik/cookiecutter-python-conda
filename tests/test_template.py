import os
import pytest


def test_cookiecutter_default(cookies):
    """test cookiecutter

    The cookies.bake() method generates a new project from your template based
    on the default values specified in cookiecutter.json
    (from https://github.com/hackebrot/pytest-cookies)
    """
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'repository_name'
    assert result.project.isdir()


@pytest.fixture
def context_all_no():
    return {
        "author_name": "the name",
        "author_email": "the.name@the_mail.com",
        "github_username": "thegithubuser",
        "repo_name": "Repo_Name",
        "project_initial_version": "10.1.99",
        "use_ci": "n",
        "use_black": "n",
        "use_bumpversion": "n"
    }


def test_cookiecutter_all_no(cookies, context_all_no):
    result = cookies.bake(extra_context=context_all_no)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'repo_name'
    assert result.project.isdir()

    repo_files = os.listdir(result.project)
    files_should_be_gone = [
        '.bumpversion.cfg',
        '.travis.yaml',
        '.pre-commit-config.yaml'
    ]
    for fname in files_should_be_gone:
        assert fname not in repo_files
