import numpy as np


def __normalize__(dataset, n_dataset, n, m):
    '''
    Метод нормализации исходных данных
    :param dataset: исходные данные
    :param n_dataset: нормализированные исходные данные
    :param n: высота матрицы
    :param m: ширина матрицы
    :return: нормализированные исходные данные
    '''
    for j in range(m):
        sq = np.sqrt(sum(dataset[:, j] ** 2))
        n_dataset[:, j] = [dataset[i, j] / sq for i in range(n)]
    return n_dataset


def __get_worst_best__(signs, dataset, m):
    '''
    Метод поиска лучшей и худшей альтернативы
    :param signs: список знаков (отрицательный или положительный критерий)
    :param dataset: исходные данные
    :param m: ширина матрицы
    :return: лучшая и худшая альтернативы
    '''
    worst = []
    best = []
    for i in range(m):
        fir, sec = (max(dataset[:, i]), min(dataset[:, i])) if signs[i] == 1 else (min(dataset[:, i]), max(dataset[:, i]))
        worst.append(sec)
        best.append(fir)
    return worst, best


def __get_worst_best_distanse__(dataset, worst, best, n):
    '''
    Метод поиска "дистации" до худшего и лучшего элементов
    :param dataset: исходные данные
    :param worst:худшая альтернатива
    :param best: лучшая альтернативы
    :param n: высота матрицы
    :return: "дистация" до худшего и лучшего элементов
    '''
    worst_dist = (dataset - worst) ** 2
    best_dist = (dataset - best) ** 2
    worst_dist = np.array([sum(worst_dist[i, :]) ** 0.5 for i in range(n)])
    best_dist = np.array([sum(best_dist[i, :]) ** 0.5 for i in range(n)])
    return worst_dist, best_dist


def __topsis__(dataset, weights, signs):
    '''
    Внутренний TOPSIS метод для сравнения альтернатив по весам
    :param dataset: исходные данные
    :param weights: список весов
    :param signs: список знаков (отрицательный или положительный критерий)
    :return: список ценности альтернатив
    '''
    dataset = np.array(dataset, dtype=float)
    n, m = len(dataset), len(dataset[0])
    n_dataset = np.empty((n, m), np.float64)
    n_dataset = __normalize__(dataset, n_dataset, n, m) * weights
    (worst, best) = __get_worst_best__(signs, n_dataset, m)
    (worst_dist, best_dist) = __get_worst_best_distanse__(n_dataset, worst, best, n)
    return worst_dist / (best_dist + worst_dist)

def prepare_info(res_dataset):
    '''
    Метод создания текстовой строки отчета
    :param res_dataset: результаты
    :return:
    '''
    max_ind = np.argmax(res_dataset)
    min_ind = np.argmin(res_dataset)
    max_info = f'Alternative №{max_ind + 1} is the best. It has score = {res_dataset[max_ind]:.4f}'
    min_info = f'Alternative №{min_ind + 1} is the worst. It has score = {res_dataset[min_ind]:.4f}'
    res = [f'Alternative №{i + 1} = {x:.4f}' for i, x in enumerate(res_dataset)]
    res.append(max_info)
    res.append(min_info)
    res = '\n'.join(res)
    print('---------TOPSIS METHOD---------\n')
    print(res)


def topsis(dataset, weights, signs):
    '''
    TOPSIS метод для сравнения альтернатив по весам
    :param dataset: исходные данные
    :param weigths: список весов
    :param signs: список знаков (отрицательный или положительный критерий)
    :return: список ценности альтернатив
    '''
    res_dataset = __topsis__(dataset, weights, signs)
    prepare_info(res_dataset)
    return res_dataset
