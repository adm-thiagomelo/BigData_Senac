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

-- IMPORTAÇÃO VIA CÓDIGO NÃO FUNCIONOU

-- CRIANDO A ENTIDADE CLIENTE:
CREATE TABLE Clientes (
id_cliente VARCHAR(10),
nome VARCHAR(100),
email VARCHAR(30)
);

-- CRIANDO A ENTIDADE PROMOVIDA PEDIDOS:

CREATE TABLE Pedidos (
id_pedido VARCHAR(10),
id_cliente VARCHAR(10),
data_pedido DATE,
valor_total DECIMAL(10,2),
id_produto VARCHAR(10),
quantidade SMALLINT
);

-- OPÇÕES DE CONSTRUÇÃO DE CHAVES:
-- 1 - DESDE O CREATE TABLE

CREATE TABLE Pedidos (
id_pedido INT AUTO_INCREMENT PRIMARY KEY,
data_pedido DATE,
valor_total DECIMAL(10,2),
id_cliente INT,
id_produto INT,
quantidade INT,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- 2 - A PARTIR DO ALTER TABLE:
ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_produtos
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

ALTER TABLE produtos
ADD CONSTRAINT pk_produtos
PRIMARY KEY (id_produto);

ALTER TABLE clientes
ADD CONSTRAINT pk_clientes
PRIMARY KEY (id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT pk_pedidos
PRIMARY KEY (id_pedido);