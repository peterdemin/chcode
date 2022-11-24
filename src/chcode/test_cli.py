from click.testing import CliRunner

from chcode.cli import run


def test_run():
    runner = CliRunner()
    result = runner.invoke(
        run,
        ["arg_value('setup', 'name', 'chcode')", "-"],
        input='setup(name="__TARGET__".format(x=123))',
    )
    assert result.stdout == "setup(name='chcode')\n"
