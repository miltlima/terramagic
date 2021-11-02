# Terramagic CLI


## Motivation

Every time , I needed create a terraform files to a new project, and a new terraform files., but this is not good. and now we have a Terramagic tool to help us to create a terraform files.

## Requirements

- Python 3.9 >=

## How to install?

```shell
pip install terramagic
```

## Hands on

[![asciicast](https://asciinema.org/a/xeSFySIjxwGK4x4m83y8BfbZY.png)](https://asciinema.org/a/xeSFySIjxwGK4x4m83y8BfbZY)

## Check the version

```shell
terramagic --version

 _____                   __  __             _      
|_   _|__ _ __ _ __ __ _|  \/  | __ _  __ _(_) ___ 
  | |/ _ \ '__| '__/ _` | |\/| |/ _` |/ _` | |/ __|
  | |  __/ |  | | | (_| | |  | | (_| | (_| | | (__ 
  |_|\___|_|  |_|  \__,_|_|  |_|\__,_|\__, |_|\___|
                                      |___/        


TerraMagic is a tool for creating a structure of folders and files for Terraform
Author: https://github.com/miltlima
Version: 0.0.9
```

## Usage(Ex.)

```shell
terramagic create-project --name=<project_name> --env=<env>
```

```shell
terramagic create-project --name=terraform --env=prod --env=dev
```

## How to use this tool ?

```shell
Usage: terramagic create-project [OPTIONS]


Options:
  -n, --name TEXT  Name of the project
  -e, --env TEXT   Environment name(dev, test, prd)
  --help           Show this message and exit.
```

Enjoy!
