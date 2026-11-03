import sqlite3

from config import DATABASE, STAGING, INTERMEDIATE, CORE
from validations import validar_modelos

def atualizar_modelos():
  arqs = [
    STAGING / "stg_alunos.sql",
    STAGING / "stg_planos.sql",
    STAGING / "stg_matriculas.sql",
    STAGING / "stg_pagamentos.sql",
    STAGING / "stg_presencas.sql",
    INTERMEDIATE / "int_matriculas_detalhadas.sql",
    INTERMEDIATE / "int_alunos_frequencia.sql",
    INTERMEDIATE / "int_alunos_frequencia_mensal.sql",
    CORE / "dim_aluno.sql",
    CORE / "dim_plano.sql",
    CORE / "fato_frequencia_mensal.sql",
    CORE / "fato_matricula.sql",
    CORE / "fato_pagamento.sql",
    CORE / "fato_presenca.sql"
  ]

  consultas = []
  for arq in arqs:
    print(f"Lendo: {arq.name}")
    sql = arq.read_text(encoding="utf-8-sig").strip()
    consultas.append(sql + "\n;")

  script = (
    "BEGIN TRANSACTION;\n"
    + "\n\n".join(consultas)
    + "\nCOMMIT;"
  )

  conn = sqlite3.connect(DATABASE)
  try:
    print("Executando modelos...")
    conn.executescript(script)
    validar_modelos(conn)
    conn.commit()
    print("Modelos executados com sucesso.")
  except Exception:
    conn.rollback()
    print("Falha na execução dos modelos. Alterações foram revertidas.")
    raise
  finally:
    conn.close()

if __name__ == "__main__":
  atualizar_modelos()