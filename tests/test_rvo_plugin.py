from click.testing import CliRunner
from mtcli_rvo.commands.rvo import rvo

def test_cli_calc_help():
    runner = CliRunner()
    result = runner.invoke(rvo, ["calc", "--help"])
    assert result.exit_code == 0
    assert "Calcula e exibe o indicador RVO" in result.output
