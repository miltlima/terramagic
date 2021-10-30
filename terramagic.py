import click
import os

from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint
from libs import datalib

@click.group()
def cli():
    pass

def create_module(name):
    pass

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(cprint(figlet_format("TerraMagic-cli", font="slant"), "magenta"))
    click.echo("A Project for create structure folders and files for Terraform")
    click.echo("Author: https://github.com/miltlima")
    click.echo("Version: 0.3")
    ctx.exit()


@click.command()
@click.option("--project-name", "-n", default="None", help="Name of the project")
@click.option("--provider","-p",default="None",help="Provider Name(AWS, Azure, GCP)")
@click.option("--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True, help="Show version")
@click.option("--module" "-m", default="None", help="Module name")
def main(project_name, provider):
    """ 
    TerraMagic-cli is a tool for creating a structure of folders and files for Terraform
    """
    try:
        os.mkdir(project_name)
        os.chdir(project_name)
        match provider:
            case ("AWS"|"Azure"|"GCP"|"OCI"|"aws"|"azure"|"gcp"|"oci"):
                datalib.modules()
                for file in datalib.files:
                    open(file, "w+")
                click.echo(f"Created terraform file for {provider} ☁️ ")
                os.chdir("..")
            case _ :
                for file in datalib.files:
                    open(file, "w+")
                click.echo("Created common terraform file")
                os.chdir("..")

    except FileExistsError:
        click.echo("The directory already exists")

if __name__ == "__main__":
    main()
