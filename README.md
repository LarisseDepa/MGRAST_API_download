## MG-RAST API Sequence Downloader

Este script automatiza o download de sequências nos estágios 050.1 e 299.1 do MG-RAST usando sua API pública. Ele aceita um arquivo de texto contendo identificadores MG-RAST (um por linha) e baixa os arquivos correspondentes, salvando-os em uma pasta especificada.

### Funcionalidades:
- Faz download de sequências nos estágios 050.1 (formato FASTQ) e 299.1 (formato FASTA).
- Grava IDs que falham no download em um arquivo txt para análise posterior.

### Instruções de uso:

#### Conda:
1. Crie um ambiente virtual: `conda create -n <nome_ambiente>`
2. Ative o ambiente virtual: `conda activate <nome_ambiente>`
   - Obs. Etapa opcional

#### PIP:
1. Instale as dependências: `pip install requests argparse tqdm gzip`

#### Modo de uso:
- Execute o script: `python MGRAST_API_download.py -f ids.txt -o output_folder --failed-ids failed_metagenome_ids`
   - Obs. É exibida uma barra de progresso durante o download.

### Argumentos:

- `-f, --file`: Caminho para o arquivo de texto contendo MG-RAST IDs.
- `-o, --output`: Pasta de destino para os arquivos baixados (padrão: "output").
- `--failed-ids`: Nome do arquivo para armazenar IDs com falha no download (padrão: "failed_ids.txt").

### Mais informações:

- [Documentação da API MG-RAST](https://api.mg-rast.org/api.html#download)

