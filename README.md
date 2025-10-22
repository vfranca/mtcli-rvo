# mtcli-rvo

`mtcli-rvo` é um plugin para o ecossistema **MTCLI**, desenvolvido para calcular e exibir o **Indicador de Volume Relativo (RVO – Relative Volume Oscillator)** diretamente no terminal, com suporte a exportação de dados e integração nativa ao MetaTrader 5.

O **RVO** é uma métrica que compara o volume atual de um ativo com sua média histórica, ajudando a identificar picos de volume, confirmação de tendências e movimentos anormais de fluxo.

---

## Instalação

Clone ou copie o repositório do plugin e, dentro da pasta principal, execute:

```bash
pip install -e .
````

Isso instala o plugin em modo **editável**, permitindo atualizações automáticas no código.

Dependências principais:

* MetaTrader5
* click
* pandas
* mtcli

---

## Estrutura do projeto

```
mtcli_rvo/
├── __init__.py
├── plugin.py          # CLI principal (Click)
├── rvo_model.py       # Cálculo do RVO
├── rvo_controller.py  # Lógica de orquestração
├── rvo_view.py        # Exibição e exportação
└── tests/
    └── test_rvo_plugin.py
```

---

## Uso via terminal

### Comando principal

```bash
mt rvo calc SYMBOL [OPTIONS]
```

### Parâmetros

| Parâmetro           | Tipo      | Padrão | Descrição                                                                               |
| ------------------- | --------- | ------ | --------------------------------------------------------------------------------------- |
| `SYMBOL`            | argumento | —      | Símbolo do ativo (ex: WINZ25, WDOX25, PETR4)                                            |
| `--timeframe`, `-t` | string    | `M5`   | Timeframe (ex: M1, M5, M15, H1, D1)                                                     |
| `--periodos`, `-p`  | inteiro   | `20`   | Número de períodos para a média de volume                                               |
| `--historico`, `-h` | inteiro   | `5`    | Número de candles exibidos no histórico                                                 |
| `--volume`, `-v`    | string    | `tick` | Tipo de volume a utilizar: `tick` (número de negócios) ou `real` (volume real em lotes) |
| `--export`, `-e`    | flag      | —      | Exporta o histórico do RVO para arquivo CSV                                             |
| `--json`, `-j`      | flag      | —      | Exporta o histórico do RVO em formato JSON                                              |

---

## Exemplos

### Cálculo simples do RVO

```bash
mt rvo calc WINZ25 -t M15 -p 20 -h 8
```

### Usando volume real (em lotes)

```bash
mt rvo calc WDOX25 -t M15 -p 20 -v real
```

### Exportar resultado em CSV

```bash
mt rvo calc WDOX25 -t H1 -p 30 -e
```

### Exportar resultado em JSON

```bash
mt rvo calc PETR4 -t D1 -p 50 -j
```

### Exportar CSV e JSON simultaneamente

```bash
mt rvo calc WINZ25 -t M5 -p 20 -h 10 -e -j
```

---

## Exemplo de saída no terminal

```
Indicador de Volume Relativo (RVO)
Símbolo: WINZ25
Timeframe: M15
Tipo de volume: tick
Volume atual: 2,350
Volume médio: 1,460
RVO atual: 1.61 — acima da média

Histórico recente do RVO:
  21/10 09:45 — 0.84 →
  21/10 10:00 — 0.95 ↑ (+13.1%)
  21/10 10:15 — 1.12 ↑ (+17.9%)
  21/10 10:30 — 1.38 ↑ (+23.2%)
  21/10 10:45 — 1.61 ↑ (+16.7%)

CSV exportado para: C:\Users\Valmir\cli\rvo_WINZ25_M15.csv
JSON exportado para: C:\Users\Valmir\cli\rvo_WINZ25_M15.json
```

---

## Conceito: RVO (Relative Volume Oscillator)

O **RVO** compara o **volume atual** com a **média de volume** de um determinado número de períodos anteriores:

[
RVO = \frac{\text{Volume Atual}}{\text{Volume Médio}}
]

* **RVO > 1.0** → Volume atual acima da média (alta participação)
* **RVO < 1.0** → Volume atual abaixo da média (baixa atividade)

O cálculo pode ser feito com:

* **Volume tick** → número de transações por candle
* **Volume real** → volume financeiro ou em lotes (quando disponível via corretora)

---

## Testes automatizados

O plugin inclui testes com **pytest** e **click.testing**.

Execute os testes com:

```bash
pytest -v
```

Exemplo de teste incluso:

```python
from click.testing import CliRunner
from mtcli_rvo.plugin import cli

def test_cli_calc_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["calc", "--help"])
    assert result.exit_code == 0
    assert "--volume" in result.output
    assert "Calcula e exibe o indicador RVO" in result.output
```

---

## Integração com o MTCLI

O plugin é registrado automaticamente pelo método `register(cli)` dentro de `plugin.py`:

```python
def register(cli):
    cli.add_command(calc)
```

Isso permite a integração direta com o comando principal do `mtcli`:

```bash
mt rvo calc WINZ25 -t M5 -v tick
```

---

## Licença

Este projeto é distribuído sob a licença **GPL-3.0**.
Consulte o arquivo `LICENSE` para mais informações.

```
