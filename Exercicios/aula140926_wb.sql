-- CRIAR BANCO DE DADOS

CREATE DATABASE meu_ecommerce;

USE meu_ecommerce;

-- CRIAR A ENTIDADE PRODUTOS

CREATE TABLE Produtos (
id_produto VARCHAR(10),
nome VARCHAR(100),
categoria VARCHAR(50),
preco DECIMAL(8, 2),
estoque INT
);

-- REMOVER TABELA/CONTEÚDO DE TABELA
DROP TABLE Produtos;

--
SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE 'C:\\Users\\melo.thiago\\Documents\\bigData\\BigData_Senac\\Exercicios\\vendas_produtos.csv' -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente
