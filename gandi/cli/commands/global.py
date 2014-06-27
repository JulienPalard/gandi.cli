
import click

from gandi.cli.core.cli import cli
from gandi.cli.core.utils import output_generic
from gandi.cli.core.params import pass_gandi


@cli.command()
@pass_gandi
def setup(gandi):
    """ Initialize Gandi CLI configuration.

    Create global configuration directory with API credentials
    """
    intro = """Welcome to GandiCLI, let's configure a few things before we \
start
"""

    outro = """
Setup completed. You can now:
* use 'gandi' to see all commands
* use 'gandi vm' to create and access a VM
* Go to https://wiki.gandi.net/cli for more info
"""
    gandi.echo(intro)
    gandi.init_config()
    gandi.echo(outro)


@cli.command()
@click.option('-g', help='edit global configuration (default=local)',
              is_flag=True, default=False)
@click.argument('key')
@click.argument('value')
@pass_gandi
def config(gandi, g, key, value):
    """Configure default values"""
    gandi.configure(global_=g, key=key, val=value)


@cli.command()
@pass_gandi
def api(gandi):
    """Display information about API used."""

    output_keys = ['api_version']

    result = gandi.api.info()
    output_generic(gandi, result, output_keys)

    return result