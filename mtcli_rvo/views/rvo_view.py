import click
import pandas as pd
import json
import os
from datetime import datetime
from mtcli.logger import setup_logger

log = setup_logger()

def exibir_rvo(dados: dict, timeframe: str, export: bool = False, json_out: bool = False):
    """Exibe o RVO formatado e exporta para CSV/JSON conforme opções."""
    symbol = dados["symbol"]
    rvo_atual = dados["rvo_atual"]
    vol_atual = dados["volume_atual"]
    vol_medio = dados["volume_medio"]
    historico = dados["historico"]

    direcao = "acima da média" if rvo_atual > 1 else "abaixo da média"
    cor_direcao = "green" if rvo_atual > 1 else "red"

    click.echo(click.style("\nIndicador de Volume Relativo (RVO)", fg="cyan", bold=True))
    click.echo(click.style(f"Ativo: {symbol}", fg="yellow"))
    click.echo(f"Timeframe: {timeframe}")
    click.echo(f"Volume atual: {vol_atual:,.0f}")
    click.echo(f"Volume médio: {vol_medio:,.0f}")
    click.echo(click.style(f"RVO atual: {rvo_atual:.2f} — {direcao}", fg=cor_direcao))

    click.echo(click.style("\nHistórico recente do RVO:", bold=True))
    linhas = []
    rvo_anterior = None

    for item in historico:
        ts = datetime.fromtimestamp(item["time"])
        valor = item["rvo"]

        seta = ""
        delta = ""
        if rvo_anterior is not None:
            if valor > rvo_anterior:
                seta = click.style("↑", fg="green")
            elif valor < rvo_anterior:
                seta = click.style("↓", fg="red")
            else:
                seta = click.style("→", fg="yellow")

            variacao = ((valor - rvo_anterior) / rvo_anterior) * 100
            delta = f"{variacao:+.1f}%"
        else:
            delta = "—"

        click.echo(f"  {ts:%d/%m %H:%M} — {valor:.2f} {seta} ({delta})")
        linhas.append({
            "datetime": ts.isoformat(),
            "rvo": round(valor, 4),
            "delta_%": delta,
        })
        rvo_anterior = valor

    # Exportar CSV
    if export:
        nome_arquivo = f"rvo_{symbol}_{timeframe}.csv"
        df = pd.DataFrame(linhas)
        df.to_csv(nome_arquivo, index=False)
        click.echo(click.style(f"\nCSV exportado para: {os.path.abspath(nome_arquivo)}", fg="cyan"))
        log.info(f"Arquivo CSV exportado: {nome_arquivo}")

    # Exportar JSON
    if json_out:
        nome_arquivo = f"rvo_{symbol}_{timeframe}.json"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(linhas, f, ensure_ascii=False, indent=2)
        click.echo(click.style(f"💾 JSON exportado para: {os.path.abspath(nome_arquivo)}", fg="cyan"))
        log.info(f"Arquivo JSON exportado: {nome_arquivo}")
