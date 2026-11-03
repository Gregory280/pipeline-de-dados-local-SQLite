CREATE TABLE fato_frequencia_mensal (
	aluno_id,
	data_referencia TEXT NOT NULL,
	ano INTEGER NOT NULL,
	mes INTEGER NOT NULL,
	dias_frequentados INTEGER NOT NULL,
	PRIMARY KEY (aluno_id, data_referencia)
);