# Dicionário de dados — Bem-Estar Academia

## 1. Identificação

- **Projeto:**  Pipeline_Local_de_Dados
- **Responsável pela documentação:** Gregory
- **Última atualização:** 06-10-2026
- **Versão:** 1.1
- **Escopo:** Fontes em formato Excel utilizadas pelo pipeline local em SQLite.


## 2. Mapeamento das Origens


| Id | Nome | Filename | Empresa | Área responsável | Periodicidade | Método de Extração |
|---|---|---|---|---|---|---|
| 01 | Alunos | alunos.xlsx | próprio | gestão da academia | semanal | arquivo |
| 02 | Planos | planos.xlsx | próprio | gestão da academia | semanal | arquivo |
| 03 | Matrículas | matriculas.xlsx | próprio | gestão da academia | semanal | arquivo |
| 04 | Pagamentos | pagamentos.xlsx | próprio | financeiro | semanal | arquivo |
| 05 | Presenças | presencas.xlsx | próprio | gestão da academia | semanal | arquivo |

## 3. Detalhamento das fontes

### Alunos

Tabela contendo informações de cadastro de pessoas que se inscreveram na academia, incluindo alunos ativos e inativos. 

- **Finalidade:** Registrar os dados cadastrais dos alunos, permitindo identificá-los e relacioná-los às suas matrículas e presenças.
- **Granularidade:** 1 linha = 1 aluno cadastrado
- **Chave identificadora:** `aluno_id`. Deve ser único e obrigatório.
- **Como o registro é criado:** Cadastro realizado na recepção utilizando o sistema de gestão da academia. Renovações utilizam o cadastro existente.
- **Como o registro é atualizado ou excluído:** Quando há necessidade de alterações cadastrais, como celular, e-mail ou endereço. O encerramento da matrícula não exclui o cadastro de aluno.
- **Formato das datas e horários:** `data_matricula` e `data_nascimento` representam datas sem horário, estando armazenadas como números seriais do Excel.
- **Moeda e unidades:** Não possui.

**Colunas**

| Coluna na fonte | Descrição | Tipo observado | Tipo esperado | Obrigatório? | Chave | Domínio, formato ou unidade | Observações |
|---|---|---|---|---|---|---|---|
| aluno_id | Identificador único do aluno | Número sequencial | INTEGER | Sim | PK | Identificador não vazio e único | Preservar zeros à esquerda. Usar o mesmo tipo nas fontes relacionadas. |
| nome | Nome do aluno registrado no cadastro | Texto | TEXT | Sim | — | Texto não vazio | — |
| email | Endereço de e-mail informado pelo aluno | Texto | TEXT | Sim | — | Endereço de e-mail não vazio | Padronizar espaços e letras minúsculas |
| telefone | Telefone de contato informado pelo aluno | Texto | TEXT | Sim | — | Telefone com DDD | Remover caracteres de formatação. Aceitar somente 11 dígitos, caso contrário colocar NULL |
| sexo | Informação de sexo registrada no cadastro | Texto | TEXT | Sim | — | Preenchimento por M, F e Não informado | Não inferir o sexo pelo nome, deixar Não informado como valor válido. |
| data_nascimento | Data de nascimento do aluno | Númerico | Data, armazenada como texto ISO no SQLite | Sim | — | AAAA-MM-DD | Gerar a data de nascimento a partir dos dias calculados do Excel |
| cidade | Cidade de residência informada pelo aluno | Texto | TEXT | Sim | — | Mesma cidade da academia | — |
| estado | Unidade federativa de residência do aluno | Texto | TEXT | Sim | — | Sigla de UF brasileira, com duas letras | — |
| data_matricula | Data da primeira inscrição do aluno na academia | Númerico | Data, armazenada como texto ISO no SQLite | Sim | — | AAAA-MM-DD | Não representa todas as contratações ou renovações. Esse histórico pertence à fonte matriculas. |
| status | Situação atual do aluno no cadastro | Texto | TEXT | Sim | — | Ativo ou Inativo, conforme categorias confirmadas na fonte | Confirmar o critério operacional. |

**Categorias e códigos**

| Coluna | Valor observado | Significado | Confirmado por / referência |
|---|---|---|---|---|
| status | Ativo | Possui uma matrícula vigente nessa data | Sistema |
| status | Inativo | Não possui matrícula vigente, pois ela terminou ou foi cancelada | Sistema |



### Planos

**Descrição e contexto**

- **Finalidade:** Informações individuais dos planos disponíveis para frequentar a academia.
- **Granularidade:** 1 linha = 1 plano
- **Chave identificadora:** `plano_id`. Deve ser único e obrigatório.
- **Como o registro é criado:** Criação manual no sistema.
- **Como o registro é atualizado ou excluído:** Edição manual no sistema.
- **Formato das datas e horários:** Não possui.
- **Moeda e unidades:** Valores monetários em reais brasileiros (BRL).

**Colunas**

| Coluna na fonte | Descrição | Tipo observado | Tipo esperado | Obrigatório? | Chave | Domínio, formato ou unidade | Observação |
|---|---|---|---|---|---|---|---|---|
| plano_id | Identificador único do plano | Númerico sequencial | INTEGER | Sim | PK | Número inteiro positivo e único | Usar o mesmo tipo em matriculas e pagamentos. Se houver códigos com letras ou zeros significativos, utilizar TEXT. |
| nome_plano | Nome comercial do plano oferecido pela academia | Texto | TEXT | Sim | — | Texto não vazio | — |
| tipo | Categoria do plano | Texto | TEXT | Sim | — | Básico ou Premium | — |
| duracao_meses | Duração contratual do plano em meses | Númerico | INTEGER | Sim | — | 1, 3, 6 ou 12 meses, conforme o catálogo | Deve ser um inteiro positivo. |
| valor_mensal | Valor mensal previsto no catálogo do plano | Númerico | REAL | Sim | — | BRL; valor positivo com duas casas decimais | Não representa o valor total do contrato nem o valor efetivamente recebido. |



### Matrículas

**Descrição e contexto**

- **Finalidade:** Registros de matrículas dos alunos que estão ativos e inativos
- **Granularidade:** 1 linha = 1 matrícula de 1 aluno
- **Chave identificadora:** `matricula_id`. Deve ser único e obrigatório.
- **Como o registro é criado:** Sistema cria após confirmar o pagamento
- **Como o registro é atualizado ou excluído:** Edições automáticas pelo sistema
- **Formato das datas e horários:** `data_inicio`, `data_fim` e `data_prevista` representam datas sem horário, estando armazenadas como números seriais do Excel.
- **Moeda e unidades:** Não possui.


**Colunas**

| Coluna na fonte | Descrição | Tipo observado | Tipo esperado | Obrigatório? | Chave | Domínio, formato ou unidade | Observações |
|---|---|---|---|---|---|---|---|
| matricula_id | Identificador único da contratação de um plano | Númerico sequencial | INTEGER | Sim | PK | Inteiro positivo e único | Cada contratação ou renovação gera uma nova matrícula. |
| aluno_id | Identificador do aluno que contratou o plano | Númerico | Mesmo tipo de alunos.aluno_id | Sim | FK | Identificador existente na fonte alunos | Deve corresponder a um aluno cadastrado. |
| plano_id | Identificador do plano contratado | Númerico | Mesmo tipo de planos.plano_id | Sim | FK | Identificador existente na fonte planos | Deve corresponder a um plano do catálogo. |
| data_inicio | Data de início da vigência da matrícula | Númerico | Data, armazenada como texto ISO no SQLite | Sim | — | Formato AAAA-MM-DD | Converter números seriais do Excel quando necessário. |
| data_fim | Data de término da vigência, considerando eventual cancelamento | Númerico | Data, armazenada como texto ISO no SQLite | Sim | — | Formato AAAA-MM-DD | Nesta simulação, também está preenchida para matrículas ativas, podendo ser futura. Deve ser posterior à data_inicio. O dia de término não faz parte da vigência. |
| data_fim_prevista | Data de término originalmente prevista para o contrato | Númerico | Data, armazenada como texto ISO no SQLite | Sim | — | Formato AAAA-MM-DD | Preserva o término planejado. Em um cancelamento antecipado, data_fim será anterior a esta data. |
| status | Situação da matrícula na data de referência da fonte | Texto | TEXT | Sim | — | Ativa, Encerrada ou Cancelada | — |
| motivo_cancelamento | Motivo registrado para o cancelamento da matrícula | Texto | TEXT | Condicional: Sim quando Cancelada | — | Texto; NULL quando não houver cancelamento | — |



### Pagamentos

**Descrição e contexto**

- **Finalidade:** Registrar as cobranças mensais vinculadas às matrículas e sua situação financeira.
- **Granularidade:** 1 linha = 1 cobrança mensal.
- **Chave identificadora:** `pagamento_id`. Deve ser único e obrigatório.
- **Como o registro é criado:** O módulo financeiro do sistema de gestão gera uma cobrança para cada período mensal da matrícula.
- **Como o registro é atualizado ou excluído:** Quando ocorre o pagamento, são atualizados o valor recebido, a data de pagamento, a forma de pagamento e o status.
- **Formato das datas e horários:** `data_vencimento` e `data_pagamento` representam datas sem horário, estando armazenadas como números seriais do Excel.
- **Moeda e unidades:** Valores monetários em reais brasileiros (BRL).

**Colunas**

| Coluna na fonte | Descrição | Tipo observado | Tipo esperado | Obrigatório? | Chave | Domínio, formato ou unidade | Observação |
|---|---|---|---|---|---|---|---|
| pagamento_id | Identificador único da cobrança | Númerico sequencial | INTEGER | Sim | PK | Inteiro positivo e único | Identifica também cobranças ainda não pagas. |
| aluno_id | Identificador do aluno responsável pela cobrança | Númerico | Mesmo tipo de alunos.aluno_id | Sim | FK | Identificador existente na fonte alunos | Deve corresponder ao aluno associado à matrícula informada. |
| matricula_id | Identificador da matrícula que originou a cobrança | Númerico | Mesmo tipo de matriculas.matricula_id | Sim | FK | Identificador existente na fonte matriculas | Permite identificar o contrato associado à cobrança. |
| plano_id | Identificador do plano associado à cobrança | Númerico | Mesmo tipo de planos.plano_id | Sim | FK | Identificador existente na fonte planos | Deve corresponder ao plano da matrícula |
| competencia | Mês de referência da cobrança | Texto | Data, armazenada como texto ISO no SQLite | Sim | — | AAAA-MM | Não representa necessariamente o mês do recebimento |
| valor | Valor monetário cobrado | Númerico | REAL | Sim | — | BRL; valor positivo com duas casas decimais | — |
| valor_pago | Valor monetário recebido para a cobrança | Númerico | REAL | Sim | — | BRL; valor positivo com duas casas decimais | Nesta simulação, é zero quando não pago e igual a valor quando pago. Zero não significa informação ausente. |
| data_vencimento | Data limite para pagamento da cobrança | Númerico | Data, armazenada como texto ISO no SQLite | Sim | — | Data no formato AAAA-MM-DD | Converter o serial do Excel para formato de data |
| data_pagamento | Data em que o pagamento foi realizado | Númerico | Data, armazenada como texto ISO no SQLite | Condicional: Sim quando Pago | — | Data no formato AAAA-MM-DD | — |
| forma_pagamento | Meio utilizado para realizar o pagamento | Texto | TEXT | Sim | — | PIX, Cartão de crédito, Cartão de débito ou Dinheiro; NULL quando não pago | — |
| status | Situação financeira da cobrança na data de referência | Texto | TEXT | Sim | — | Pago, Atrasado ou Em aberto | — |


**Categorias e códigos**

Preencha quando houver status, categorias ou códigos. Diferencie os valores encontrados dos valores oficialmente permitidos.

| Coluna | Valor observado | Significado | Confirmado por / referência |
|---|---|---|---|
| status | Pago | houve quitação | Módulo financeiro |
| status | Atrasado | não pago e vencimento anterior à data de referência | Módulo financeiro |
| status | Em aberto | não pago e ainda não vencido | Módulo financeiro |



### Presenças

**Descrição e contexto**

- **Finalidade:** Registra a atividade de quem frequenta a academia
- **Granularidade:** 1 linha = 1 presença
- **Chave identificadora:** presenca_id
- **Como o registro é criado:** Sistema X instalado físcamente na academia
- **Formato das datas e horários:** `data` e `hora_entrada` em formato númerico do Excel
- **Moeda e unidades:** Não possui

**Colunas**

| Coluna na fonte | Descrição | Tipo observado | Tipo esperado | Obrigatório? | Chave | Domínio, formato ou unidade | Observações |
|---|---|---|---|---|---|---|---|
| presenca_id | Identificador único do registro de entrada na academia | A confirmar | INTEGER | Sim | PK | Inteiro positivo e único | Identifica uma entrada, não um dia de frequência. |
| aluno_id | Identificador do aluno que realizou a entrada | A confirmar | Mesmo tipo de alunos.aluno_id | Sim | FK | Identificador existente na fonte alunos | Deve corresponder ao aluno associado à matrícula informada. |
| matricula_id | Identificador da matrícula vinculada à entrada | A confirmar | Mesmo tipo de matriculas.matricula_id | Sim | FK | Identificador existente na fonte matriculas | A presença deve ocorrer durante a vigência da matrícula: data_inicio ≤ data da presença < data_fim. |
| data | Data em que o aluno entrou na academia | A confirmar; pode ser número serial do Excel | TEXT | Sim | — | Data no formato AAAA-MM-DD | Converter números seriais do Excel para data. Não deve ser posterior à data de referência da extração. |
| hora_entrada | Horário em que o aluno entrou na academia | Número decimal representando uma fração do dia | TEXT | Sim | — | Horário no formato HH:MM:SS | Multiplicar a fração por 86400, arredondar para segundos e converter para horário. Aceitar valores numéricos de 0, inclusive, até 1, exclusive. Zero representa meia-noite. |
| modalidade | Atividade associada ao registro de presença | A confirmar | TEXT | Sim | — | Musculação, Funcional, Spinning ou Yoga | Padronizar espaços e grafia. Nesta simulação, planos Básicos permitem Musculação; planos Premium permitem as quatro modalidades. |


## 4. Histórico de alterações

| Data | Alteração | Responsável |
|---|---|---|
| 07-10-2026 | Criação do dicionário de dados | Gregory N. M. |
| 02-11-2026 | Devido à natureza de como SQLite trata o campo data foi modificado a forma como queremos armazena-lá. |
