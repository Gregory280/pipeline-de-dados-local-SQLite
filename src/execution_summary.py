import sqlite3
from config import DATABASE

def mostrar_resumo(duracao):
  grupos = {
    "TABELAS RAW": [
      "raw_alunos",
      "raw_planos",
      "raw_matriculas",
      "raw_pagamentos",
      "raw_presencas",
    ],

    "DIMENSÕES": [
      "dim_aluno",
      "dim_plano",
      "dim_data",
    ],

    "FATOS": [
      "fato_matricula",
      "fato_pagamento",
      "fato_presenca",
      "fato_frequencia_mensal",
    ],
  }

  conn = sqlite3.connect(DATABASE)

  try:
    print("\n========== RESUMO DA EXECUÇÃO ==========")
    for grupo, tabelas in grupos.items():
      print(f"\n{grupo}")
      for tabela in tabelas:
        quantidade = conn.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()[0]
        quantidade_formatada = (f"{quantidade:,}".replace(",", "."))
        print(
          f"  {tabela}: "
          f"{quantidade_formatada} registros"
        )
    print(f"\nDuração da carga: {duracao:.2f} segundos")
    print("=======================================")

  finally:
    conn.close()