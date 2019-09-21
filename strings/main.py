import argparse
import os

from lib.string_formatter import format_text

DEFAULT_LINE_SIZE = 40

"""
    Configuração dos argumentos de linha de comando:
    --line-size: Tamanho máximo permitido para as linhas. O padrão é 40 caracteres.
    --justify: Flag opcional que informa se o texto deve ser justificado ou não. Padrão é falso
    --input-file: Arquivo de entrada contendo o texto para formatação. Exemplo: input.txt
    --output-file: Arquivo de saída para escrita do texto formatado. Opcional. Caso não seja fornecido,
    os dados são exibidos no terminal.
    
"""

argument_parser = argparse.ArgumentParser(
    "main.py",
    description=
"""
    Efetua a formatação do arquivo informado seguindo a parametrização fornecida. Por padrão o script 
    usa o tamanho máximo da linha de 40 caracteres, não justifica o texto e imprime o resultado 
    na saída padrão.
"""
)
argument_parser.add_argument("--line-size", help="Tamanho máximo da linha.", type=int,
                             default=DEFAULT_LINE_SIZE)
argument_parser.add_argument("--justify", help="Aplica a formatação justificada ao texto de entrada.",
                             action="store_true", default=False)
argument_parser.add_argument("--input-file", required=True, help="Arquivo contendo o texto para formatação.")
argument_parser.add_argument("--output-file", help="Arquivo de saída para o texto formatado.", default=None)
args = argument_parser.parse_args()

if not os.path.exists(args.input_file):
    print(f'O arquivo de entrada "{args.input_file}" não foi encontrado. Verifique as informações.')
    quit(1)


with open(args.input_file, 'rb') as i_stream:
    text = i_stream.read().decode()

formatted_text = format_text(text, args.line_size, args.justify)

if args.output_file:
    with open(args.output_file, 'wb') as o_stream:
        o_stream.write(formatted_text.encode())
else:
    print(formatted_text)
