WITH contagens AS (
  SELECT
    (SELECT COUNT(*) FROM stg_alunos) AS origem,
    (SELECT COUNT(*) FROM dim_aluno) AS destino

  UNION ALL

  SELECT
    (SELECT COUNT(*) FROM stg_planos),
    (SELECT COUNT(*) FROM dim_plano)

  UNION ALL

  SELECT
    (SELECT COUNT(*) FROM int_matriculas_detalhadas),
    (SELECT COUNT(*) FROM fato_matricula)

  UNION ALL

  SELECT
    (SELECT COUNT(*) FROM stg_pagamentos),
    (SELECT COUNT(*) FROM fato_pagamento)

  UNION ALL

  SELECT
    (SELECT COUNT(*) FROM stg_presencas),
    (SELECT COUNT(*) FROM fato_presenca)

  UNION ALL

  SELECT
    (SELECT COUNT(*) FROM int_alunos_frequencia_mensal),
    (SELECT COUNT(*) FROM fato_frequencia_mensal)
)

SELECT
    COUNT(*) AS quantidade_erros
FROM contagens
WHERE origem <> destino;