"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.group(context_settings=CONTEXT_SETTINGS)
# @click.option('--version', '-v', help='Get package version')
def cli():
    """A simple command line tool."""
    pass


@cli.command('run', short_help='Runs the application.')
# @click.version_option()
def run(args=None):

    click.echo('Running the application')
    from {{cookiecutter.project_slug}} import main
    # Launch application through URL or filetype.
    # click.launch("https://click.palletsprojects.com/")
    click.echo('Exiting the application')
    return 0

# cli.add_command(hello)
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
