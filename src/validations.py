from config import VALIDATIONS

def validar_modelos(conexao):
  arquivos = [
    VALIDATIONS / "validar_quantidade.sql",
    VALIDATIONS / "validar_total_pagamentos.sql",
  ]
  print("\nIniciando validações...")
  for arquivo in arquivos:
    sql = arquivo.read_text(encoding="utf-8-sig")
    cursor = conexao.execute(sql)
    resultado = cursor.fetchone()

    if resultado is None:
      raise ValueError(f"Validação sem resultado: {arquivo.name}")
    colunas = [
      coluna[0]
      for coluna in cursor.description
    ]

    if "quantidade_erros" not in colunas:
      raise ValueError(f"Coluna quantidade_erros ausente: {arquivo.name}")

    indice = colunas.index("quantidade_erros")
    quantidade_erros = resultado[indice]

    if quantidade_erros is None:
      raise ValueError(f"Validação retornou NULL: {arquivo.name}")

    if quantidade_erros != 0:
      raise ValueError(
        f"Validação reprovada: {arquivo.name}. "
        f"Resultado: {quantidade_erros}."
      )

    print(f"OK | {arquivo.name}")

  print("Todas as validações passaram.")