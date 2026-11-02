DROP VIEW IF EXISTS stg_matriculas;

CREATE VIEW stg_matriculas AS

SELECT
  matricula_id,
  aluno_id,
  plano_id,
  DATE(data_inicio) AS data_inicio,
  DATE(data_fim) AS data_fim,
  DATE(data_fim_prevista) AS data_fim_prevista,
  status,
  motivo_cancelamento
FROM
  raw_matriculas;
  