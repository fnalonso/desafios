from argparse import ArgumentParser

from util import SubredditsAction

arg_parser = ArgumentParser("nada_pra_fazer", "Retorna as threads mais populares nos subreddits solicitados")
arg_parser.add_argument(
    "--subreddits", type=str, required=True, action=SubredditsAction,
    help="Lista de subreddits para pesquisa separados por ';'.",
)

arguments = arg_parser.parse_args()
print(arguments)