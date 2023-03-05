import os
import shutil
import subprocess
from pathlib import Path
from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint
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
    click.echo("Version: 1.4")
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
        click.echo(f"Created {e} environment.")


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
def remove(name):
    """Delete the project"""
    project_dir = Path(name)
    if project_dir.is_dir():
        click.confirm(
            click.style(f"Are you sure you want to delete {name}?", fg="blue"),
            abort=True,
        )
        shutil.rmtree(project_dir)
        click.secho(f"Project {name} deleted successfully", fg="green")
    else:
        click.secho(f"Project {name} not found", fg="red")


@main.command()
@click.option(
    "--name", "-n", help="Name of the project", prompt=True, confirmation_prompt=True
)
def check(name):
    """Check all files inside a Terraform project are valid."""
    project_dir = Path(name)
    if not project_dir.is_dir():
        click.secho(f"Project {name} not found", fg="red")
        return
    os.chdir(name)
    success = True
    results = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".tf"):
                try:
                    subprocess.check_output(
                        ["terraform", "validate", os.path.join(root, file)]
                    )
                    results.append(f"✔️ {os.path.join(root, file)}")
                except subprocess.CalledProcessError as e:
                    success = False
                    results.append(
                        f"❌ {os.path.join(root, file)} - {e.output.decode('utf-8').strip()}"
                    )
    if success:
        print("Check succeeded")
    else:
        print("Check failed with the following results:")
        for result in results:
            print(result)
        click.secho(
            "Please inspect and solve the above issues before continuing", fg="yellow"
        )


if __name__ == "__main__":
    main(prog_name="terramagic cli tool")
