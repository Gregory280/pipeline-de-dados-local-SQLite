DROP VIEW IF EXISTS stg_pagamentos;

CREATE VIEW stg_pagamentos AS

SELECT
  pagamento_id,
  aluno_id,
  matricula_id,
  plano_id,
  STRFTIME('%m/%Y', JULIANDAY('1899-12-30') + competencia) AS competencia,
  ROUND(valor, 2) AS valor,
  ROUND(valor_pago, 2) AS valor_pago,
  DATE(data_vencimento) AS data_vencimento,
  DATE(data_pagamento) AS data_pagamento,
  forma_pagamento,
  status
FROM
  raw_pagamentos;
