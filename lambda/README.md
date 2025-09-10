# Lambda - ClimaConecta ⚡

## Descrição

Esta pasta contém a função **AWS Lambda** utilizada no projeto **ClimaConecta**.  
A função é responsável por processar os dados do INPE (PRODES e DETER), gerar gráficos e armazená-los no **Amazon S3** para posterior visualização no site.

---

## Uso da Layer

A **Layer** necessária já está disponível neste repositório como o arquivo **`layer.zip`**.  
Devido ao tamanho (cerca de **70 MB**), o GitHub não permite a visualização do conteúdo, mas o arquivo pode ser baixado normalmente.

### Passos para usar:

1. **Baixar o repositório**  
   - Clone o projeto:  
     ```bash
     git clone https://github.com/Erick-Fanka/clima-conecta.git
     ```
   - Ou faça o download manual no GitHub (botão verde **Code → Download ZIP**).

2. **Enviar o arquivo para o Amazon S3**  
   ```bash
   aws s3 cp lambda/layer.zip s3://seu-bucket/
