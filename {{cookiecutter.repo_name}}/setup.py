from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.project_initial_version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    license="MIT",
    description="{{ cookiecutter.project_short_description }}",
    # long_description=description,
    # url='https://...',
    package_dir={"": "src"},
    packages=find_packages("./src"),
    include_package_data=True,
    install_requires=[
        # 'dep1>=1.0,<2',
        # 'dep2>=2'
    ],
    entry_points={
        "console_scripts": ["{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.__main__:main"]
    },
)
