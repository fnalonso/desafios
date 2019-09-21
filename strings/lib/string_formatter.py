import re


def format_text(text, line_size, justify):
    """
    Efetua a formatação de um texto especificado
    :param text: str contendo o texto para formataçao
    :param line_size: tamanho máximo da linha
    :param justify: se True justifica o texto. O padrão é Falso
    :return: str contendo o texto formatado.
    """
    # Remove as quebras de linha contidas no texto
    clean_text = re.sub(r'\r\n', '', text)
    current_line_size = 0
    formatted_lines = []
    formatted_line = []
    for word in clean_text.split(' '):
        # O tamanho é calculado adicionando 1, pois toda palavra na sentença possui ao menos um espaço
        word_length = len(word) + 1
        """
            Se o tamanho atual da linha for menor que o tamanho máximo e o tamanho atual somada a 
            palavra forem menores que o tamanho máximo, adiciona a palavra na frase e adiciona o 
            tamanho da mesma na contagem do tamanho da linha
        """
        if current_line_size < line_size and current_line_size + word_length <= line_size:
            # Adiciona apenas a palavra no inicio da lista
            if not formatted_line:
                formatted_line.append(word)
            else:
                formatted_line.append(" ")
                formatted_line.append(word)

            current_line_size += word_length
        else:
            if justify:
                """
                    Faz a formatação justificada do texto.
                    1 - Calcula a quantidade de espaços necessários para igualar o tamanho das linhas
                    2 - Enquanto não preencher a diferença itera os elementos da linha
                """
                space_left = line_size - current_line_size
                while space_left > 0:
                    for item in formatted_line:
                        item_idx = formatted_line.index(item)
                        # Se o item não for um espaço e nem o ultimo elemento, adiciona um espaço na frente.
                        # a adição de espaço é sempre da esquerda para a direita
                        if item != " " and (item_idx != len(formatted_line) - 1):
                            formatted_line.insert(formatted_line.index(item) + 1, " ")
                            space_left -= 1
                        if space_left == 0:
                            break

            # Insere a linha formatada na lista do texto formatado.
            formatted_lines.append(formatted_line)
            formatted_line = [word]
            current_line_size = word_length
    else:
        formatted_lines.append(formatted_line)


    output = ""
    for line in formatted_lines:
        output += "".join(line) + "\n"

    return output