DELETE FROM fato_frequencia_mensal;

INSERT INTO fato_frequencia_mensal (
    aluno_id,
    data_referencia,
    ano,
    mes,
    dias_frequentados
)

SELECT
    aluno_id,
    data_referencia,
    ano,
    mes,
    dias_frequentados
FROM int_alunos_frequencia_mensal;