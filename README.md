## MG-RAST API Download

Este script automatiza o download de sequências nos estágios 050.1 e 299.1 do MG-RAST usando sua API pública. Ele aceita um arquivo de texto contendo identificadores MG-RAST (um por linha) e baixa os arquivos correspondentes, salvando-os em uma pasta especificada.

### Funcionalidades:
- Faz download de sequências nos estágios 050.1 e 299.1 (formato FASTQ e FNA).
- Grava IDs que falham no download em um arquivo txt para análise posterior.

### Instruções de uso:

#### Conda:
1. Crie um ambiente virtual: `conda create -n <nome_ambiente>`
2. Ative o ambiente virtual: `conda activate <nome_ambiente>`
   - Obs. Etapa opcional

#### PIP:
1. Instale as dependências: `pip install requests argparse tqdm gzip`

#### Modo de uso:
- Execute o script: `python MGRAST_API_download.py -f ids.txt -o output_folder --failed-ids failed_metagenome_ids.txt`
   - Obs. É exibida uma barra de progresso durante o download.

### Argumentos:

- `-f, --file`: Caminho para o arquivo de texto contendo MGRAST METAGENOME IDs. 
- `-o, --output`: Nome da pasta de destino para os arquivos baixados.
- `--failed-ids`: Nome do arquivo para armazenar IDs com falha no download.
- 
#### Exemplo de arquivo de entrada (input)  `ids.txt:`
`mgm4502539`

`mgm4502540`

`mgm4502541`

Obs. É uma lista com metagenoma id...
### Descompactar os aquivos gz:
Exemplo: `gzip -d id_050.1.fastq.gz` ou  `gzip -d id_299.1.fastq.gz`

### Mais informações:

- [Documentação da API MG-RAST](https://api.mg-rast.org/api.html#download)

## Aviso de Uso

Ao utilizar este código ou realizar modificações no mesmo, é obrigatório citar as autoras Larisse Depa e Larissa Depa como contribuidoras originais.

Por favor, reconheça a autoria ao incorporar ou adaptar este código em seus próprios projetos. 


