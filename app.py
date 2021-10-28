import click
import os

from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint
from libs import providers_file


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(cprint(figlet_format("TerraMagic-cli", font="slant"), "magenta"))
    click.echo("A Project for create structure folders and files for Terraform")
    click.echo("Author: https://github.com/miltlima")
    click.echo("Version: 0.3")
    ctx.exit()


@click.command()
@click.option("--name", "-n", default="None", help="Name of the project")
@click.option("--provider","-p",default="None",help="Provider Name(AWS, Azure, GCP)")
@click.option("--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def main(name, provider):
    """ 
    TerraMagic-cli create structure folders and files for Terraform

    """
    try:
        os.mkdir(name)
        os.chdir(name)
        providers_file.modules()
        if provider != "":
            for file in providers_file.files:
                open(file, "w+")
            click.echo(f"Created terraform file to ☁️  {provider}")
            os.chdir("..")
    
    except FileExistsError:
        click.echo("The directory already exists")
    

    


if __name__ == "__main__":
    main()
