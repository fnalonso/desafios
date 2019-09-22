import re
from collections import namedtuple

import requests
from bs4 import BeautifulSoup


REDDIT_BASE_URL = "https://old.reddit.com"
DEFAULT_PAGE_SIZE = 25

SubredditData = namedtuple('SubredditData', ['subreddit', 'name', 'score', 'comments'])


class NadaParaFazer(object):

    def __init__(self, subreddits: list):
        """
        Classe do crawler do reddit.
        :param subreddits: Lista contendo os subreddits para pesquisa
        """
        self.subreddits = subreddits

    def get_bombando(self, score=5000):
        """
        Executa a requisição no reddit e processa o HTML recebido na resposta
        :param score: Pontuação mínima necessária para ser considerado um sucesso!
        :return: Lista de namedtuples com as informações
        """
        bombando = []
        for subreddit in self.subreddits:
            """
                Flag que determina se há necessidade de avançar para a próxima página do subreddit.
                Isto é determinado caso a página atual contenha alguma thread com a pontuação mínima
                necessária
            """
            loop = True
            subreddit_url = f"{REDDIT_BASE_URL}/r/{subreddit}"
            subreddit_params = None
            pagination_counter = 0
            after = None

            while loop:
                need_paginate = False
                subreddit_header = {
                    "User-Agent": f"NadaPraFazer {subreddit} {pagination_counter}"
                }

                if pagination_counter > 0:
                    subreddit_params = {
                        "count": pagination_counter,
                        "after": after
                    }

                subreddit_data = requests.get(
                    subreddit_url,
                    headers=subreddit_header,
                    params=subreddit_params
                ).content

                bs = BeautifulSoup(subreddit_data, 'html.parser')
                subreddit_threads = bs.find_all(attrs={'class': 'thing'})

                for thread in subreddit_threads:
                    # Inicia checando se a thread tem a pontuação minima necessária
                    thread_score = thread.find(attrs={'class': 'score likes'}).text
                    # Substituição necessária para tratar cenários onde a quantidade de likes
                    # tem a representação abreviada como 13.2K
                    if "k" in thread_score:
                        thread_score = float(thread_score.replace('k', '')) * 1000
                    else:
                        # Se for uma thread com pontuação não numérica, atribui 0 a pontuação
                        if re.match(r'\D', thread_score):
                            thread_score = 0
                        else:
                            thread_score = int(thread_score)

                    if thread_score < score:
                        continue
                    need_paginate = True
                    """
                         Titulo da thread
                        normaliza o texto removendo quebras de linha, tabulações ou sequencias de espaço
                    """
                    thread_name = re.sub(
                        r'[\t\s]+', ' ', re.sub(r'\n', '', thread.find('a', attrs={'class': 'title'}).text)
                    )

                    # link para os comentários
                    thread_comments = thread.find('li', attrs={'class': 'first'}).find('a')['href']

                    bombando.append(
                        SubredditData(subreddit, thread_name, thread_score, thread_comments)
                    )

                    # Id da thread, utilizando quando ocorre a necessidade de ir para próxima página
                    after = thread.get('data-fullname')

                """
                    Nao encontrou na página atual nenhuma thread com a pontuação mínima
                    encerra o loop e avança para o próximo subreddit
                """
                if not need_paginate:
                    loop = False
                else:
                    pagination_counter += DEFAULT_PAGE_SIZE

        return bombando
