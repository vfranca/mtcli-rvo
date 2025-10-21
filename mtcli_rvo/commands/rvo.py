import click


def calcular():
    return "Funcionou!"


@click.command("rvo")
@click.version_option(package_name="plugin-exemplo")
def rvo():
    """Ajuda do comando."""
    resultado = calcular()
    click.echo(f"{resultado}")


if __name__ == "__main__":
    rvo()
