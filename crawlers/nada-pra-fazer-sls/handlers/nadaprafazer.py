import json
import os

import requests

from nada_pra_fazer import NadaParaFazer

bot_id = os.environ['bot_id']
expected_token = os.environ['expected_token']
TELEGRAM_SEND_MESSAGE_URL = f"https://api.telegram.org/bot{bot_id}/sendMessage"


def post(event, context):

    if event['pathParameters']['token'] != expected_token:
        return {
            "statusCode": 403,
            "body": json.dumps(
                {
                    "message": "Unauthorized."
                }
            )
        }

    msg_data = json.loads(event['body'])
    chat_id = msg_data['message']['chat']['id']
    received_text = msg_data['message']['text']

    if received_text == "/start":
        response_message = "Olá!! Estou pronto.\nPara se divertir muito me envie o comando /NadaPraFazer e\numa lista de subreddits separada por ';'. Por exemplo:\n/NadaPraFazer cats;dogs;birds"
    elif received_text.startswith("/NadaPraFazer"):
        try:
            _, subreddits = received_text.split(" ")
            subreddits = subreddits.split(";")
            npf = NadaParaFazer(subreddits)
            bombando = npf.get_bombando()
            response_message = f"Aqui estão as threads bombando no momento nos subreddits {subreddits}:\n\n"
            thread_layout = "Titulo:<strong>{titulo}</strong>\nSubreddit: {subreddit} | Pontuação: {score}\nComentários: {comments}\n\n"
            for thread in bombando:
                response_message += thread_layout.format(
                    titulo=thread.name, subreddit=thread.subreddit, score=thread.score, comments=thread.comments
                )

        except ValueError:
            response_message = "Recebi o comando da diversão, mas ele está incorreto.\nEnvie /NadaPraFazer e a lista de subreddits separados por ';'"

    else:
        response_message = "Desculpe, mas sou um bot iniciante e apenas tenho o comando /NadaPraFazer =("

    message_body = {
        "chat_id": chat_id,
        "disable_web_page_preview": True,
        "parse_mode": "HTML",
        "text": response_message
    }

    requests.post(TELEGRAM_SEND_MESSAGE_URL, json=message_body)

    response = {
        "statusCode": 200,
        "body": json.dumps({})
    }

    return response
