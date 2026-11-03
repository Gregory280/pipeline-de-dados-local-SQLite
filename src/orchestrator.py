from time import perf_counter
from ingestion import carregar_dados
from run_models import atualizar_modelos
from execution_summary import mostrar_resumo
from backup import criar_backup

def main():
  inicio = perf_counter()
  try:
    print("\nCriando backup do banco de dados...")
    criar_backup()

    print("\nCarregando dados...")
    carregar_dados()

    print("\nExecução dos modelos...")
    atualizar_modelos()

    duracao = perf_counter() - inicio
    mostrar_resumo(duracao)

  except Exception:
    print("\nPipeline interrompido devido a erros...")
    print("Se um backup foi criado, ele foi preservado em db/backups.")
    raise
  
  print("\nPipeline concluído com sucesso...")

if __name__ == "__main__":
  main()