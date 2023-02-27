import os
import click
import shutil
from pathlib import Path
from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint

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

def print_version(ctx, value):
    """Print current version"""
    if not value or ctx.resilient_parsing:
        return
    click.echo("Version: 0.1.3")
    ctx.exit()


def create_modules():
    """Create the modules directory and its subdirectories and files"""
    Path("modules").mkdir()
    for folder in MODULES_FOLDER:
        Path(f"modules/{folder}").mkdir()
        os.chdir(f"modules/{folder}")
        for file in MODULES_FILES:
            with open(file, "w+") as handler:
                pass
        os.chdir("../..")


def create_env_folders(env):
    """Create the specified environment folders"""
    for e in env:
        Path(e).mkdir()
        click.echo(f"Created {e} folder.")


def create_env_files(env):
    """Create the terraform files for each environment"""
    for e in env:
        os.chdir(e)
        for file in PROJECT_FILES:
            with open(file, "w+") as handler:
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
            fg="green",
        )
    except FileExistsError:
        click.secho(("The directory already exists!"), bg="red")
        os.chdir("..")


@main.command()
@click.option(
    "--name", "-n", help="Name of the project", prompt=True, confirmation_prompt=True
)
@click.option("--delete", "-d", is_flag=True, help="Delete the project")
def remove(name, delete):
    """Delete the project"""
    if delete:
        if Path(name).exists():
            click.confirm(f"Are you sure you want to delete {name}?", abort=True)
            shutil.rmtree(name)
            click.secho(f"Project {name} deleted successfully", fg="green")
        else:
            click.secho(f"Project {name} not found", fg="red")
    else:
        click.secho(
            f"Delete flag not provided, project {name} cannot be deleted ", fg="red"
        )


if __name__ == "__main__":
    main()
