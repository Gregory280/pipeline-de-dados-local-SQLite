DROP VIEW IF EXISTS rpt_faturamento_mensal;

CREATE VIEW rpt_faturamento_mensal AS
SELECT
  STRFTIME('%Y-%m', data_pagamento) AS mes_referencia,
  ROUND(SUM(valor_pago), 2) AS valor_recebido
FROM
  fato_pagamento
WHERE
  data_pagamento >= DATE('now', 'localtime', 'start of year')
  AND data_pagamento < DATE('now', 'localtime', 'start of year', '+1 year')
GROUP BY
  STRFTIME('%Y-%m', data_pagamento)