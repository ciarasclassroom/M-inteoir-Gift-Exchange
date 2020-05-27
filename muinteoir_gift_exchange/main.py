import csv
import json
import os
from pathlib import Path
import random

from jinja2 import Template

import click
import keyring
import yaml

from muinteoir_gift_exchange import __version__

MODULE_NAME = __name__.split('.')[0]
CONFIG_DIR_PATH = click.get_app_dir(MODULE_NAME)
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR_PATH, 'config.yaml')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'{MODULE_NAME} {__version__}')
    ctx.exit()


@click.group()
@click.option('--config-file',
              '-c',
              help='Use alternative configuration file',
              default=CONFIG_FILE_PATH)
@click.option('-V',
              '--version',
              is_flag=True,
              callback=print_version,
              expose_value=False,
              is_eager=True,
              help='Print the current version number and exit.')
@click.pass_context
def main(ctx: click.core.Context, config_file: str):
    path = Path(config_file)
    data = {}

    if path.exists() and path.is_file():
        with open(config_file, 'rb') as fd:
            data = yaml.safe_load(fd)
    ctx.obj = {'config': data, 'config_file': path, 'config_dir': path.parent}


@main.command()
@click.argument('profile_name', nargs=-1)
@click.option('--csv-file',
              help='File from google forms containing all the entries',
              type=click.Path(),
              required=True)
@click.pass_obj
def generate(obj, profile_name, csv_file):
    entries = []
    matches = []
    template = Template(open('template.tpl').read())
    with open(csv_file) as fp:
        items = csv.reader(fp)
        for item in items:
            address = item[3].strip().replace('\n', ', ').replace(
                ',,', ',').replace(' ,,', ', ').replace(' ,', ', ').strip()
            first_name = address.split(",")[0].split(" ")[0]
            entries.append({
                "timestamp": item[0].strip(),
                "live_in_ireland": item[1].strip(),
                "instagram": item[2].strip().replace('@', ''),
                "address": address,
                "email": item[4].strip(),
                "other": item[5].strip(),
                "first_name": first_name
            })
    random.shuffle(entries)
    for index, giver in enumerate(entries):
        if index == len(entries) - 1:
            receiver = entries[0]
        else:
            receiver = entries[index + 1]
        matches.append({"gift_giver": giver, "gift_receiver": receiver})
    for match in matches:
        print(template.render(data=match))
        print("\n=======\n")
