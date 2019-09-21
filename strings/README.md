# Formatador de textos

## Informativo

O script foi implementado utilizando a versão 3.7.4 do python e o ambiente virtual é o pipenv. Para 
utiliza-lo, após o checkout do repositório, deve-se executar os comandos abaixo dentro da pasta do projeto:

    pipenv install

E para ativar o ambiente virtual:

    pipenv shell


## Utilização

O cli implementado possui alguns parâmetros de execução que são descritos utilizando o comando:

    python main.py -h

Abaixo a saída da descrição:

    usage: main.py [-h] [--line-size LINE_SIZE] [--justify] --input-file
               INPUT_FILE [--output-file OUTPUT_FILE]

    Efetua a formatação do arquivo informado seguindo a parametrização fornecida.
    Por padrão o script usa o tamanho máximo da linha de 40 caracteres, não
    justifica o texto e imprime o resultado na saída padrão.
    
    optional arguments:
      -h, --help            show this help message and exit
      --line-size LINE_SIZE
                            Tamanho máximo da linha.
      --justify             Aplica a formatação justificada ao texto de entrada.
      --input-file INPUT_FILE
                            Arquivo contendo o texto para formatação.
      --output-file OUTPUT_FILE
                            Arquivo de saída para o texto formatado.


O controle dos parâmetros do script foi feito utilizando a lib argparser.

Abaixo alguns exemplos de utilização:

    # Gerar o texto formatado com tamanho máximo de linhas de 40 caracteres
    # utilizando o arquivo de exemplo contido no repositório
    python main.py --input-file input.txt
    
    # Gerar o texto formatado com o tamanho máximo da linha em 60 caracteres e justificado
    python main.py --input-file input.txt --line-size 60 --justify
    
    # Gerar o texto formatado justificado e escreve-lo no arquivo saida.txt
    python main.py --input-file input.txt --justify --output-file saida.txt

