import os
import shutil
import subprocess
from pathlib import Path
import click


MODULES_FOLDER = ["vpc", "cluster", "instance"]
MODULES_FILES = ["main.tf", "variables.tf", "outputs.tf"]
PROJECT_FILES = [
    "main.tf",
    "variables.tf",
    "outputs.tf",
    "backend.tf",
    "main.tfvars",
    ".gitignore",
]


def print_version(ctx, param, value):
    """Print current version"""
    if not value or ctx.resilient_parsing:
        return
    click.echo("Version: 0.2.9")
    ctx.exit()


def create_project_files(base_path):
    for file in PROJECT_FILES:
        file_path = base_path / file
        with file_path.open("w+", encoding="utf-8"):
            pass

def create_modules(base_path):

    modules_path = base_path / "modules"
    modules_path.mkdir(exist_ok=True)

    for folder in MODULES_FOLDER:
        folder_path = modules_path / folder
        folder_path.mkdir(exist_ok=True)

        with folder_path:
            for file in MODULES_FILES:
                file_path = folder_path / file
                with file_path.open("w+", encoding="utf-8"):
                    pass

def create_env_folders(base_path):

    envs_path = base_path / "environments"
    envs_path.mkdir(exist_ok=True)
    envs = ["production", "development", "staging" ]
    for e in envs:
        env_path = envs_path / e
        env_path.mkdir(exist_ok=True)

        tfvars_file_path = env_path / f"{e}.tfvars"
        with tfvars_file_path.open("w", encoding="utf-8"):
            pass



@click.group()
@click.option(
    "--version",
    "-v",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show version",
)
def main():
    """ClI tool to create Terraform project"""
    pass


@main.command()
@click.option(
    "--name", "-n", help="Name of the project", prompt=True, confirmation_prompt=True
)

def create(name):
    """Create a new Terraform project with specified name and environment"""

    base_path = Path(name)
    try:
        base_path.mkdir(exist_ok=True)
        create_modules(base_path)
        create_env_folders(base_path)
        create_project_files(base_path)
        click.secho(
            (f"Created project {name} successfully, You're ready move to ☁️ !!"),
            fg="blue",
        )
    except FileExistsError:
        click.secho(("The directory already exists!"), bg="red")
        os.chdir("..")


@main.command()
@click.option(
    "--name", "-n", help="Name of the project", prompt=True, confirmation_prompt=True
)
def remove(name):
    """Delete the project"""
    project_dir = Path(name)
    if project_dir.is_dir():
        click.confirm(
            click.style(f"Are you sure you want to delete {name}?", fg="cyan"),
            abort=True,
        )
        shutil.rmtree(project_dir)
        click.secho(f"Project {name} deleted successfully !!!", fg="blue")
    else:
        click.secho(f"Project {name} not found", fg="red")


if __name__ == "__main__":
    main()
