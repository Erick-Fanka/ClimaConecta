import pandas as pd
import matplotlib.pyplot as plt
import boto3
import io
import urllib.parse
import os

def lambda_handler(event, context):
    """
    Função principal da Lambda que é ativada por um gatilho do S3.
    """
    try:
        # Extrai o nome do bucket e a chave (caminho do arquivo) do evento do S3
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        
        print(f"Iniciando o processamento do arquivo: {file_key} no bucket: {bucket_name}")
        
        s3 = boto3.client("s3")

        # Baixar o CSV do S3
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_csv(io.BytesIO(obj["Body"].read()))

        # Excluir a última linha, que contém as variações percentuais
        df = df.iloc[:-1]

        # Garantir que as colunas 'Ano' e 'AMZ_LEGAL' sejam tratadas como números
        df["Ano"] = pd.to_numeric(df["Ano"], errors='coerce')
        df["AMZ_LEGAL"] = pd.to_numeric(df["AMZ_LEGAL"], errors='coerce')
        df = df.dropna(subset=["Ano", "AMZ_LEGAL"])

        # Resultado 1: Evolução anual do desmatamento
        df_ano = df.rename(columns={"AMZ_LEGAL": "area_desmatada"})
        df_ano = df_ano[["Ano", "area_desmatada"]]

        plt.figure(figsize=(10, 5))
        plt.plot(df_ano["Ano"], df_ano["area_desmatada"], marker="o")
        plt.title("Evolução do Desmatamento (km²)")
        plt.xlabel("Ano")
        plt.ylabel("Área desmatada (km²)")
        plt.grid(True)
        plt.savefig("/tmp/evolucao.png")

        # Resultado 2: Top estados
        state_columns = ['AC', 'AM', 'AP', 'MA', 'MT', 'PA', 'RO', 'RR', 'TO']
        df_estados = df.melt(id_vars=['Ano'], value_vars=state_columns, var_name='estado', value_name='area_desmatada')
        
        df_estados['area_desmatada'] = pd.to_numeric(df_estados['area_desmatada'], errors='coerce')
        df_estados = df_estados.dropna(subset=['area_desmatada'])

        df_estado_acumulado = df_estados.groupby('estado')['area_desmatada'].sum().reset_index()
        df_estado_acumulado = df_estado_acumulado.sort_values('area_desmatada', ascending=False).head(5)

        df_estado_acumulado.plot(kind="bar", x="estado", y="area_desmatada", legend=False)
        plt.title("Top 5 Estados - Desmatamento Acumulado")
        plt.ylabel("Área desmatada (km²)")
        plt.savefig("/tmp/top_estados.png")

        # Salvar tabelas
        df_ano.to_csv("/tmp/desmatamento_por_ano.csv", index=False)
        df_estado_acumulado.to_csv("/tmp/top_estados.csv", index=False)

        # Upload para S3
        s3.upload_file("/tmp/evolucao.png", bucket_name, "analytics/evolucao.png")
        s3.upload_file("/tmp/top_estados.png", bucket_name, "analytics/top_estados.png")
        s3.upload_file("/tmp/desmatamento_por_ano.csv", bucket_name, "processed/desmatamento_por_ano.csv")
        s3.upload_file("/tmp/top_estados.csv", bucket_name, "processed/top_estados.csv")

        print("Análise concluída e arquivos enviados para o S3.")
        
        return {
            'statusCode': 200,
            'body': 'Processamento de dados concluído com sucesso.'
        }
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {
            'statusCode': 500,
            'body': 'Falha ao processar os dados.'
        }