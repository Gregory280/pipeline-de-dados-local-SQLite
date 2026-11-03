DROP VIEW IF EXISTS rpt_frequencia_media_mensal;

CREATE VIEW rpt_frequencia_media_mensal AS
SELECT
	ano,
	mes,
	COUNT(*) AS quantidade_alunos,
	SUM(dias_frequentados) AS total_dias_frequentados,
	ROUND(AVG(dias_frequentados), 2) AS media_dias_por_aluno
FROM
	fato_alunos_frequencia_mensal
GROUP BY ano, mes;