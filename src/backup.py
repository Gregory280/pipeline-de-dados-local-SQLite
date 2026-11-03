import sqlite3
from config import BACKUPS, DATABASE

def criar_backup():
  if not DATABASE.is_file():
    print("Nenhum backup foi criado.")
    return None
  BACKUPS.mkdir(parents=True, exist_ok=True)
  caminho_backup = BACKUPS / "warehouse_backup.db"
  origem = None
  destino = None

  try:
    origem = sqlite3.connect(DATABASE.resolve().as_uri() + "?mode=ro", uri=True)
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
  return caminho_backup