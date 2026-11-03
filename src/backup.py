import sqlite3
from datetime import datetime

from config import DATABASE, BACKUPS


def criar_backup():
  if not DATABASE.is_file():
    print("Banco ainda não existe. Nenhum backup foi criado.")
    return None

  BACKUPS.mkdir(parents=True, exist_ok=True)
  data_hora = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
  caminho_backup = BACKUPS / f"warehouse_{data_hora}.db"
  origem = None
  destino = None

  try:
    origem = sqlite3.connect(
      DATABASE.resolve().as_uri() + "?mode=ro",
      uri=True,
    )
    destino = sqlite3.connect(caminho_backup)
    origem.backup(destino)

  except Exception:
    if destino is not None:
      destino.close()
      destino = None

    caminho_backup.unlink(missing_ok=True)
    raise

  finally:
    if destino is not None:
      destino.close()
    if origem is not None:
      origem.close()
  
  print(f"Backup criado: {caminho_backup.name}")

  backups = sorted(
    BACKUPS.glob("warehouse_*.db"),
    key=lambda arquivo: arquivo.stat().st_mtime_ns,
    reverse=True,
  )

  for arquivo in backups[2:]:
    arquivo.unlink()
    print(f"Backup antigo removido: {arquivo.name}")

  return caminho_backup