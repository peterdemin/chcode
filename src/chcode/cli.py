import io
import json

import click

from chcode.loader import ASTLoader
from chcode.source_changer_factory import build_source_changer


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '-i', '--in-place', default=False, is_flag=True, help='Save changes in the source file.'
)
@click.argument('code')
@click.argument('source', type=click.File('rt', encoding='utf-8'))
def run(in_place: bool, code: str, source: io.TextIOWrapper):
    """Execute CODE on SOURCE."""
    result = exec_code(code, source.read())
    source.close()
    if in_place:
        with open(source.name, "wt", encoding='utf-8') as fobj:
            fobj.write(result)
    else:
        click.echo(result)


@cli.command()
@click.argument('source', type=click.File('rt', encoding='utf-8'))
def ast(source):
    """Print Abstract Syntax Tree for SOURCE."""
    click.echo(load_ast(source.read()))


def exec_code(code: str, source: str) -> str:
    source_changer = build_source_changer(source)
    namespace = {'source_changer': source_changer}
    bytecode = compile('source_changer.' + code, '-', mode='eval')
    return eval(bytecode, {}, namespace)  # pylint: disable=eval-used


def load_ast(source: str) -> str:
    return json.dumps(ASTLoader()(source), indent=2)


def main() -> None:
    cli()


if __name__ == '__main__':
    main()
