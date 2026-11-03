DROP VIEW IF EXISTS kpi_presencas_mes_atual;

CREATE VIEW kpi_presencas_mes_atual AS
SELECT
	COUNT(*) AS total_presencas_mes_atual
FROM fato_presenca
WHERE data >= DATE('now', 'localtime', 'start of month') AND data < DATE('now', 'localtime', '+1 day');