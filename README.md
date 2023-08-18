[!["Buy Me A Coffee"](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/miltlima)

# Terramagic CLI

Terramagic is a command-line interface tool that makes it easy to create and manage Terraform projects.

## Motivation

Creating a new Terraform project from scratch can be time-consuming and error-prone. With Terramagic, you can quickly generate a template for your project and customize it to your needs.

### Requirements

Python 3.9 or higher

### Installation

You can easily install Terramagic using pip:

```shell
pip3 install terramagic
```

### Usage

#### Creating a new project

To create a new Terraform project, use the create command:

```shell
terramagic create --name <project_name> --env <environment_name>
```

For example, to create a project called "myapp" with two environments ("dev" and "prod"), run:

```shell
terramagic create --name myapp --env dev --env prod
```

This will generate a new directory called "myapp" with the following structure:

```code
myapp/
├── dev.tfvars
├── main.tf
├── outputs.tf
├── prod.tfvars
└── variables.tf
```

You can then edit these files to define your infrastructure resources and variables.

#### Deleting a project

To delete an existing project, use the delete command and specify the project name:

```shell
terramagic delete --name <project_name>
```

For example, to delete the "myapp" project, run:

```shell
terramagic delete --name myapp
```

Help
For detailed information about available commands and options, run:

```shell
terramagic --help
```

This will display the following message:

```shell
Usage: terramagic [OPTIONS] COMMAND [ARGS]...

  ClI tool to create Terraform project

Options:
  -v, --version  Show version
  --help         Show this message and exit.

Commands:
  create  Create a new Terraform project with specified name and environment
  remove  Delete the project
```

Enjoy using Terramagic to simplify your Terraform workflow!
