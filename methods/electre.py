import numpy as np


def __normalize__(dataset):
    '''
    Метод нормализации исходных данных
    :param dataset: исходные данные
    :return: нормализированные исходные данные
    '''
    n = dataset.shape[0]
    m = dataset.shape[1]
    n_dataset = np.zeros((n, m))
    for j in range(m):
        _max = max(dataset[:, j])
        n_dataset[:, j] = [dataset[i, j] / _max for i in range(n)]
    return n_dataset


def __concordance_matrix__(dataset, weigths):
    '''
    Метод составления матрицы согласия
    :param dataset: исходные данные
    :param weigths: список весов
    :return: матрица согласия
    '''
    concordance = np.zeros((dataset.shape[0], dataset.shape[0]))
    for i in range(0, concordance.shape[0]):
        for j in range(0, concordance.shape[1]):
            concordance[i, j] = sum(weigths[k] for k in range(0, dataset.shape[1]) if (dataset[i, k] >= dataset[j, k]))
    return concordance


def __discordance_matrix__(dataset):
    '''
    Метод составления матрицы несогласия
    :param dataset: исходные данные
    :return: матрица несогласия
    '''
    n = dataset.shape[0]
    discordance = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            discordance[i, j] = round(max(dataset[j, :] - dataset[i, :]), 2)
    return discordance


# Function: Dominance Matrix
def __dominance_matrix__(concordance, discordance, c_lim, d_lim):
    '''
    Метод составления матрицы удовлетворения пороговым значения индексов согласия и несогласия
    :param concordance: матрица согласия
    :param discordance: матрица несогласия
    :param c_lim: пороговое значение индекса согласия
    :param d_lim: пороговое значение индекса несогласия
    :return: матрица удовлетворения пороговым значения индексов согласия и несогласия
    '''
    dominance = np.zeros((concordance.shape[0], concordance.shape[0]))
    for i in range(0, dominance.shape[0]):
        for j in range(0, dominance.shape[1]):
            if concordance[i, j] >= c_lim and discordance[i, j] <= d_lim and i != j:
                dominance[i, j] = 1
    return dominance


def __lim_concordance_list__(concordance):
    '''
    Метод поиска предельных значений индекса согласия
    :param concordance: матрица согласия
    :return: список предельных значений индекса согласия
    '''
    return [round(min(x), 4) for x in concordance]


def __lim_discordance_list__(discordance):
    '''
    Метод поиска предельных значений индекса несогласия
    :param discordance: матрица несогласия
    :return: список предельных значений индекса несогласия
    '''
    return [round(max(x), 4) for x in discordance]


def __prepare_text_info__(dominance):
    '''
    Метод создания текстовой строки отчета
    :param dominance: матрица удовлетворения пороговым значения индексов согласия и несогласия
    :return: строка о выборе альтернатив
    '''
    dominated = [(f'Alternative №{i + 1}', elem) for i, elem in enumerate(dominance)]
    dominated = sorted(dominated, key=lambda k: sum(k[1]), reverse=True)
    info = '---------ELECTRE METHOD---------\n'
    for ind, el in enumerate(dominated):
        info += f'Place {ind + 1}: {el[0]}\n'
    return info


def electre(dataset, weigths, c_lim=0.45, d_lim=0.5):
    '''
    ELECTRE I метод для сравнения альтернатив по весам
    :param dataset: исходные данные
    :param weigths: список весов
    :param c_lim: пороговое значение индекса согласия
    :param d_lim: пороговое значение индекса несогласия
    :return: матрица согласия, матрица несогласия,
    матрица удовлетворения пороговым значения индексов согласия и несогласия
    '''
    dataset = np.array(dataset)
    dataset = __normalize__(dataset)
    concordance = __concordance_matrix__(dataset, weigths)
    discordance = __discordance_matrix__(dataset)
    dominance = __dominance_matrix__(concordance, discordance, c_lim, d_lim)
    print(__prepare_text_info__(dominance))
    return concordance, discordance, dominance

