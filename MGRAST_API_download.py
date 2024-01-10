#!/usr/bin/python3
"""
Autoras: Larisse Depa e Larissa Depa
Script para baixar sequências nos estágios 050.1 e 299.1 do MG-RAST.
Para mais detalhes sobre o uso da API, consulte: https://api.mg-rast.org/api.html#download
Version 1.0

RUN: python MGRAST_API_download.py -f ids.txt -o output_folder --failed-ids failed_metagenome_ids.txt


"""

import argparse
import os
import requests
import gzip
from tqdm import tqdm

# Variáveis para os nomes dos arquivos
file_name_050 = "050.1"
file_name_299 = "299.1"


def download_mgrast_sequence(mg_id, file_name, output_folder, file_extension):
    # Construir URL de download
    download_url = f"https://api-ui.mg-rast.org/download/{mg_id}.3?file={file_name}"

    try:
        # Tentar fazer o download do arquivo
        print(f"Iniciando download de {mg_id}_{file_name}...")
        response = requests.get(download_url, stream=True)
        response.raise_for_status()

        # Criar pastas se não existirem
        folder_path = os.path.join(output_folder, file_name)
        os.makedirs(folder_path, exist_ok=True)

        # Obter o tamanho total do arquivo
        total_size = int(response.headers.get('content-length', 0))

        # Criar a barra de progresso
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

        # Salvar o arquivo com a extensão desejada
        file_path = os.path.join(folder_path, f"{mg_id}_{file_name}.{file_extension}.gz")
        with gzip.open(file_path, "wb") as gz_file:
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    gz_file.write(chunk)
                    progress_bar.update(len(chunk))

        progress_bar.close()
        print(f"Download concluído: {mg_id}_{file_name}.{file_extension}")
        return True, file_path
    except requests.exceptions.HTTPError as err:
        print(f"Falha no download: {mg_id}_{file_name}.{file_extension}. Código de status: {err.response.status_code}")
        return False, None


def download_mgrast_sequences(ids, output_folder, failed_ids_file):
    print("Download iniciado...")

    for mg_id in ids:
        # Tenta baixar o arquivo "050.1" com a extensão "fastqc"
        success_050, file_path = download_mgrast_sequence(mg_id, file_name_050, output_folder, file_extension="fastq")

        # Se falhar, tenta baixar o arquivo "299.1" com a extensão "fna"
        if not success_050:
            success_299, file_path = download_mgrast_sequence(mg_id, file_name_299, output_folder, file_extension="fna")

            # Se ambos falharem, registra o ID que falhou em um arquivo
            if not success_299:
                with open(failed_ids_file, "a") as failed_file:
                    failed_file.write(f"{mg_id}\n")


def main():
    # Configurar o parser de argumentos de linha de comando
    parser = argparse.ArgumentParser(description="Download de sequências do MG-RAST.")
    parser.add_argument("-f", "--file", required=True, help="Arquivo no formato txt contendo IDs do MG-RAST (um por linha)")
    parser.add_argument("-o", "--output", default="output", help="Pasta de saída para as sequências baixadas")
    parser.add_argument("--failed-ids", default="failed_ids.txt", help="Arquivo para armazenar IDs que falharam no download")
    args = parser.parse_args()

    # Ler IDs do arquivo
    with open(args.file, "r") as file:
        mg_ids = [line.strip() for line in file.readlines()]

    # Criar o arquivo failed_ids.txt se não existir
    open(args.failed_ids, 'a').close()

    # Chamar a função para baixar as sequências
    download_mgrast_sequences(mg_ids, args.output, args.failed_ids)


if __name__ == "__main__":
    main()
