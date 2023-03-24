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
    click.echo("Version: 0.1.8")
    ctx.exit()


def create_modules():
    """Create the modules directory and its subdirectories and files"""
    Path("modules").mkdir()
    for folder in MODULES_FOLDER:
        Path(f"modules/{folder}").mkdir()
        os.chdir(f"modules/{folder}")
        for file in MODULES_FILES:
            with open(file, "w+", encoding="utf-8") as handler:
                pass
        os.chdir("../..")


def create_env_folders(env):
    """Create the specified environment folders"""
    for e in env:
        Path(e).mkdir()


def create_env_files(env):
    """Create the terraform files for each environment"""
    for e in env:
        os.chdir(e)
        for file in PROJECT_FILES:
            with open(file, "w+", encoding="utf-8") as handler:
                pass
        os.chdir("..")


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
@click.option(
    "--env",
    "-e",
    help="Environment name(dev, stg, prd)",
    prompt=True,
    multiple=True,
)
def create(name, env):
    """Create a new Terraform project with specified name and environment"""
    try:
        Path(name).mkdir()
        os.chdir(name)
        create_modules()
        create_env_folders(env)
        create_env_files(env)
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
