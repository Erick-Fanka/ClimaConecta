# ClimaConecta 🌱☁️

## Descrição

O **ClimaConecta** é um projeto acadêmico que demonstra a aplicação prática da **computação em nuvem** para o monitoramento do **desmatamento na Amazônia**.  
O projeto utiliza **arquitetura serverless na AWS** para processar e visualizar dados ambientais de forma escalável, automática e acessível, contribuindo para a **conscientização ambiental** e a **democratização do acesso à informação**.

**Observação:** Este trabalho foi desenvolvido em **escala reduzida**, pois se trata de um projeto escolar realizado em laboratório. Devido a limitações do ambiente, a coleta de dados foi feita **manualmente** e algumas funcionalidades, como o uso do **CloudFront**, não puderam ser implementadas.

## Estrutura do Repositório
ClimaConecta/
│
├── lambda/ # Função Lambda, gatilho e explicações das layers
├── s3/ # Estrutura de pastas simulando o bucket S3 (dados e gráficos)
├── site/ # Página web estática (index.html e arquivos HTML)
├── README.md # Este arquivo

## Funcionalidades

- Coleta manual de dados do **INPE** (PRODES e DETER), adaptada à escala do laboratório.  
- Processamento de dados via **AWS Lambda** usando Python e bibliotecas como **Pandas** e **Matplotlib**.  
- Armazenamento de dados em **Amazon S3**.  
- Geração de gráficos e dashboards em uma **página web estática**.  
- Visualização de tendências de desmatamento em tempo quase real.  

## Tecnologias Utilizadas

- **AWS Lambda (Serverless)**  
- **Amazon S3**  
- **Python** (Pandas, Matplotlib)  
- **HTML/CSS** para dashboards estáticos  


### Detalhes das pastas

#### lambda/
- Contém a função Lambda que processa os dados do INPE (PRODES e DETER).  
- Inclui o gatilho que ativa a função quando novos dados são carregados.  
- Possui arquivo `.md` explicando o uso de **Layers** e dependências Python.

#### s3/
- Simula a estrutura do bucket S3 com **pastas para dados** e **gráficos gerados**.  
- Serve como referência para organização e armazenamento dos arquivos processados.

#### site/
- Contém o **index.html** e outros arquivos HTML necessários para visualizar os dashboards.  
- Mostra os gráficos e informações processadas pela função Lambda.

---

## Tecnologias Utilizadas

- **AWS Lambda (Serverless)**  
- **Amazon S3**  
- **Python** (Pandas, Matplotlib)  
- **HTML/CSS** para dashboards estáticos  

## Autor

**Erick Fanka**  
[LinkedIn](https://www.linkedin.com/in/seu-linkedin-aqui)
