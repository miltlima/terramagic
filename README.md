# Terramagic CLI

## Motivation

Every time , I needed create a terraform files to a new project, and a new terraform files., but this is not good. and now we have a Terramagic tool to help us to create a terraform files.

## Requirements

- Python 3.8 >=

## How to install?

```shell
pip install terramagic
```

## Check the version

```bash
terramagic --version
```

### Create a new project

```shell
terramagic create --name <project name> --env <env>
```

```shell
terramagic create --name terraform --env prod --env dev
```

### Delete a project

```shell
terramagic delete --name <project name>
```

### Check if all terraform files configuration are valid.

```shell
terramagic check --name <project name>
```

## How to use this tool ?

```shell
Usage: terramagic [OPTIONS] COMMAND [ARGS]...

  ClI tool to create Terraform project

Options:
  -v, --version  Show version
  --help         Show this message and exit.

Commands:
  check   Check all files inside a Terraform project are valid.
  create  Create a new Terraform project with specified name and environment
  remove  Delete the project
```

Enjoy!
