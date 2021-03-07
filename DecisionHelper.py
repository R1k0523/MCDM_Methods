
import methods


class DecisionHelper:

    def __init__(self, dataset, weights, signs=None):
        """
        Конструктор
        :param dataset: исходные данные
        :param weights: список весов
        :param signs: необходимы только в методе TOPSIS
        """
        self.dataset = dataset
        self.weights = weights
        self.signs = signs if signs else [1]*len(weights)


    def topsis(self):
        """
        TOPSIS метод для сравнения альтернатив по весам
        :return: список ценности альтернатив
        """
        return methods.topsis(self.dataset, self.weights, self.signs)

    def electre(self):
        """
        ELECTRE I метод для сравнения альтернатив по весам
        :return: матрица согласия, матрица несогласия,
        матрица удовлетворения пороговым значения индексов согласия и несогласия
        """
        return methods.electre(self.dataset, self.weights)

    def saw(self):
        """
        SAW метод для сравнения альтернатив по весам
        :return: список ценности альтернатив
        """
        return methods.saw_method(self.dataset, self.weights)

