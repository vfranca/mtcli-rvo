from click.testing import CliRunner
from mtcli_rvo.commands.rvo import rvo

def test_cli_calc_help():
    runner = CliRunner()
    result = runner.invoke(rvo, ["--help"])
    assert result.exit_code == 0
    assert "--volume" in result.output or "--volume" in result.output.lower()
    assert "Calcula e exibe o indicador RVO" in result.output
