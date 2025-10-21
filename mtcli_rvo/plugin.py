from mtcli_rvo.commands.rvo import rvo


def register(cli):
    cli.add_command(rvo, name="rvo")
