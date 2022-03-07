def origem_destino_iguais(origem, destino, lista_de_erros):
    """
    Verifica se o campo origem e destino são iguais
    :param destino: str
    :param lista_erros: str
    :return: dict lista_de_erros
    """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser os mesmos'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """
    Verifica se possui algum caracter numérico
    :param valor_campo: str
    :param nome_campo: str
    :param lista_de_erros: dict
    :return: dict lista_de_erros
    """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Caracteres numéricos não são permitidos nestes campos.'


def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """
    Valida se a data de ida é maior do que a data de volta
    :param data_ida: date
    :param data_volta: date
    :param lista_de_erros: dict
    :return: dict lista_de_erros
    """

    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'A data de volta não pode ser anterior a data de ida.'

def data_menor_que_o_dia_atual(data_ida, data_atual, lista_de_erros):
    """
    Valida se a data de ida é menor que a data atual.
    :param data_ida: date
    :param data_atual: date
    :param lista_de_erros: dict
    :return: dict lista_de_erros
    """
    if data_ida < data_atual:
        lista_de_erros['data_ida'] = 'A data de ida não pode ser menor que a data atual.'