from time import time
from argparse import ArgumentParser

from util import SubredditsAction
from nada_pra_fazer import NadaParaFazer

arg_parser = ArgumentParser(
    "main.py", description="Retorna as threads mais populares nos subreddits solicitados"
)
arg_parser.add_argument(
    "--subreddits", type=str, required=True, action=SubredditsAction,
    help='Lista de subreddits para pesquisa separados por ";". Exemplo: "python;cats;dogs;askreddit"',
)
arg_parser.add_argument(
    "--score", type=int,  default=5000,
    help="Pontuação necessária para a thread ser considerada um sucesso. Valor padrão 5000."
)

arguments = arg_parser.parse_args()
npf = NadaParaFazer(arguments.subreddits)

print(f"""
CLI - Nada para fazer.

Efetuando a pesquisa dos subreddits: {arguments.subreddits} 

Pesquisa iniciada...""")

b = time()
lista_bombando = npf.get_bombando(arguments.score)
f = round(time() - b, 2)
print(f"""
Pesquisa concluída em {f} segundos com um total de {len(lista_bombando)} entradas. Listagem:  
""")

for thread in lista_bombando:
    print(f"Title: {thread.name}\nSubreddit: {thread.subreddit} | Score: {thread.score}\nComments: {thread.comments}\n")
