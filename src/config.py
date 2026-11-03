from pathlib import Path

# Caminhos

# Raiz do projeto
SOURCE = Path(__file__).resolve().parents[1]
# Banco de dados
DATABASE = SOURCE / "db" / "warehouse.db"
BACKUPS = SOURCE / "db" / "backups"
# Dados
RAW = SOURCE / "data" / "raw"
# Scripts SQL
SCHEMAS = SOURCE / "db" / "schemas"
STAGING = SOURCE / "models" / "staging"
INTERMEDIATE = SOURCE / "models" / "intermediate"
CORE = SOURCE / "models" / "marts" / "core"



