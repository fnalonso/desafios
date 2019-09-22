# Crawler

## Geral

Para utilizar o CLI, deve-se primeiramente instalar o ambiente virtual utilizando o pipenv com o commando:

    pipenv install
 
E depois ativá-lo

    pipenv shell

## Desafio 1

Para utilizar o cli, basta utilizar o comando:

    python main.py --subreddits "cats;dogs;birds"
   
É possível informar a quantidade de pontos que definem o critério para uma thread bombando, o cli dispõe de um comando
de ajuda com a seguinte saída:

    usage: main.py [-h] --subreddits SUBREDDITS [--score SCORE]

    Retorna as threads mais populares nos subreddits solicitados

    optional arguments:
    -h, --help            show this help message and exit
    --subreddits SUBREDDITS
                        Lista de subreddits para pesquisa separados por ";".
                        Exemplo: "python;cats;dogs;askreddit"
    --score SCORE         Pontuação necessária para a thread ser considerada um
                        sucesso. Valor padrão 5000.

A saída gerada é a seguinte:

    $ python main.py --subreddits cats

    CLI - Nada para fazer.
    
    Efetuando a pesquisa dos subreddits: ['cats']
    
    Pesquisa iniciada...
    
    Pesquisa concluída em 2.83 segundos com um total de 4 entradas. Listagem:
    
    Title: I love him more than my own life
    Subreddit: cats | Score: 10500.0
    Comments: https://old.reddit.com/r/cats/comments/d7ow64/i_love_him_more_than_my_own_life/
    
    Title: Whenever I tell her not to nibble/bite the mouse cord she gives me this look
    Subreddit: cats | Score: 13800.0
    Comments: https://old.reddit.com/r/cats/comments/d7fooh/whenever_i_tell_her_not_to_nibblebite_the_mouse/
    
    Title: We lost my boy this morning. He jumped up on my lap and had a sudden cardiac arrest. I tried to give him CPR but he died in my arms. I’ll miss you forever Mr. Pickle.
    Subreddit: cats | Score: 7578
    Comments: https://old.reddit.com/r/cats/comments/d7fxxr/we_lost_my_boy_this_morning_he_jumped_up_on_my/

A lib utilizada nesta etapa é a ./crawlers/nada_pra_fazer.py


## Desafio 2 

O nome do bot é @nadaprafaze_bot e este responde aos comandos "/start" e "/NadaPraFazer 'dogs;cats;birds'" sempre utilizando
o valor default de pontuação que é 5000.

A implementação foi feita utilizando o webhook para uma função lambda hospedada no AWS, o deploy da função foi efetuado
utilizando o framework serverless (serverless.com) e as bibliotecas necessárias para o funcionamento do crawler estão
em uma camada separada. A estrutura do serviço está na pasta "nada-pra-fazer-sls" e a camada dentro da pasta "layer". 
O arquivo de definição da aplicação que foi feito o deploy está no arquivo "serverless.yml" dentro da pasta "nada-pra-fazer-sls"