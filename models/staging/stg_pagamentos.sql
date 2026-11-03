DROP VIEW IF EXISTS stg_pagamentos;

CREATE VIEW stg_pagamentos AS
SELECT
    pagamento_id,
    aluno_id,
    matricula_id,
    plano_id,
    competencia,
    ROUND(valor, 2) AS valor,
    ROUND(valor_pago, 2) AS valor_pago,
    DATE(JULIANDAY('1899-12-30') + data_vencimento) AS data_vencimento,
    DATE(JULIANDAY('1899-12-30') + data_pagamento) AS data_pagamento,
    forma_pagamento,
    status
FROM raw_pagamentos;