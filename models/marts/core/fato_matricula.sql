DELETE FROM fato_matricula;

INSERT INTO fato_matricula (
    matricula_id,
    aluno_id,
    plano_id,
    data_inicio,
    data_fim,
    data_fim_prevista,
    status_matricula,
    motivo_cancelamento
)
SELECT
    matricula_id,
    aluno_id,
    plano_id,
    data_inicio,
    data_fim,
    data_fim_prevista,
    status_matricula,
    motivo_cancelamento
FROM int_matriculas_detalhadas;