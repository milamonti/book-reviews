# 📚 Análise dos Top 100 Livros em Tendência (Streamlit App)

## 📖 Descrição

Este projeto é um aplicativo web interativo, construído com **Streamlit**, para explorar e visualizar dados de uma lista de **Top 100 Livros em Tendência**, juntamente com suas avaliações e detalhes de publicação.

O objetivo é fornecer uma visão geral das tendências de publicação e preço, além de permitir uma análise detalhada das resenhas de clientes para cada livro.

## ✨ Funcionalidades

O aplicativo é estruturado com uma página principal de análise e uma página secundária de detalhes.

### 1. Página Principal: Análise Geral (`main.py`)

* **Filtro de Preço:** Permite aos usuários filtrar os livros por faixa de preço através de um controle deslizante na barra lateral.
* **Visualização de Dados:** Exibe a tabela dos livros filtrados.
* **Gráficos de Distribuição:** Apresenta visualizações dinâmicas (criadas com Plotly) sobre:
    * A distribuição da contagem de livros por **Ano de Publicação**.
    * A distribuição de **Preços** dos livros.

### 2. Página de Detalhes: Revisões de Livros (`pages/book_reviews.py`)

* **Seleção de Livro:** Permite selecionar qualquer livro da lista para uma análise aprofundada.
* **Métricas Chave:** Exibe o Preço, Classificação (Rating) e Ano de Publicação do livro selecionado.
* **Resenhas de Clientes:** Lista todas as avaliações de clientes disponíveis para o livro, apresentadas de forma clara usando componentes de mensagem de chat.

## 🛠️ Tecnologias Utilizadas

* **Streamlit:** Framework para criação de aplicativos web de dados em Python.
* **Pandas:** Biblioteca para manipulação e análise de dados (leitura dos arquivos `.csv`).
* **Plotly Express:** Biblioteca para a criação de gráficos informativos e interativos.

## 📁 Estrutura do Projeto

O projeto segue a convenção de multi-página do Streamlit, com os dados armazenados em um subdiretório.
