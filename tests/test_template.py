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
    assert result.project.basename == "name-of-the-project"
    assert result.project.isdir()

    repo_files = os.listdir(result.project)

    extra_files = [
        ".pre-commit-config.yaml",
        ".bumpversion.cfg",
        ".gitignore",
        "pyproject.toml",
        "README.md",
    ]

    for fname in extra_files:
        assert fname in repo_files


@pytest.mark.parametrize(
    "context, gone_files",
    [
        ({"use_black": "n"}, [".pre-commit-config.yaml"]),
        ({"use_ci": "n"}, []),
        ({"use_bumpversion": "n"}, [".bumpversion.cfg"]),
        ({"use_bumpversion": "n", "use_ci": "n"}, [".bumpversion.cfg"]),
        ({"use_bumpversion": "n", "use_black": "n"}, [".bumpversion.cfg", ".pre-commit-config.yaml"]),
        ({"use_black": "n", "use_ci": "n"}, [".pre-commit-config.yaml"]),
        (
            {"use_bumpversion": "n", "use_black": "n", "use_ci": "n"},
            [".bumpversion.cfg", ".pre-commit-config.yaml"],
        ),
    ],
)
def test_post_gen(cookies, context, gone_files):
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()

    repo_files = os.listdir(result.project)
    for fname in gone_files:
        assert fname not in repo_files
