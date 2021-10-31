import click
import os

from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint
from libs import datalib


@click.group()
def main():
    pass


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(cprint(figlet_format("TerraMagic", font="slant"), "magenta"))
    click.echo(

        "TerraMagic-cli is a tool for creating a structure of folders and files for Terraform"
    )
    click.echo("Author: https://github.com/miltlima")
    click.echo("Version: 0.0.2")
    ctx.exit()


@main.command()
@click.option("--name", "-n", help="Name of the project")
@click.option("--env", "-e", help="Environment name(dev, test, prd)", multiple=True)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show version",
)
def create_project(name, env):
    try:
        os.mkdir(name)
        os.chdir(name)
        if env:
            for e in env:
                os.mkdir(e)
                os.chdir(e)
                datalib.modules()
                for file in datalib.files:
                    open(file, "w+")
                os.chdir("..")
            click.echo(
                click.style(
                    (f"Created project {name} successfully, You're ready move to ☁️ !!"),
                    fg="green",
                )
            )
        else:
            click.echo(click.style((f"Environment {env} not found"), fg="red"))

    except FileExistsError:
        click.echo(click.style(("The directory already exists!"), bg="red"))
        os.chdir("..")


if __name__ == "__main__":
    main()
