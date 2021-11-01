# Terramagic CLI

```shell
  ______                     __  ___            _                 ___ 
 /_  __/__  ______________ _/  |/  /___ _____ _(_)____      _____/ (_)
  / / / _ \/ ___/ ___/ __ `/ /|_/ / __ `/ __ `/ / ___/_____/ ___/ / / 
 / / /  __/ /  / /  / /_/ / /  / / /_/ / /_/ / / /__/_____/ /__/ / /  
/_/  \___/_/  /_/   \__,_/_/  /_/\__,_/\__, /_/\___/      \___/_/_/   
                                    /____/                 
```

## Motivation

Every time , I needed create a terraform files to a new project, and a new terraform files., but this is not good. and now we have a Terramagic tool to help us to create a terraform files.

## Requirements

- Python 3.9 >=

## How to install?

Clone this project to folder you preference:

```shell
https://github.com/miltlima/terramagic
```

Enter in folder

```shell
cd terramagic
```

ATTENTION: you need install pip packages.

## How to install these pip packages ?

```shell
pip install -r requirements.txt
```

Add permissions in file

```shell
chmod +x terraform_magic.py
```

Move file to system PATH:

```shell
sudo mv terraform_magic.py /usr/local/bin/terramagic
```

## How to use this tool ?

```shell
Usage: terramagic.py create-project [OPTIONS]

  TerraMagic-cli is a tool to creating a structure of folders and files to a terraform project.


Options:
  -n, --name TEXT  Name of the project
  -e, --env TEXT   Environment name(dev, test, prd)
  -v, --version    Show version
  --help           Show this message and exit.
```

Enjoy!
