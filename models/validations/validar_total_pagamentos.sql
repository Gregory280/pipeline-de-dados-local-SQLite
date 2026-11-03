WITH totais AS (
  SELECT
    (
      SELECT COALESCE(SUM(valor_pago), 0)
      FROM stg_pagamentos
    ) AS total_staging,

    (
      SELECT COALESCE(SUM(valor_pago), 0)
      FROM fato_pagamento
    ) AS total_fato
)

SELECT
  CASE
    WHEN ABS(total_staging - total_fato) > 0.01
      THEN 1
    ELSE 0
  END AS quantidade_erros
FROM totais;