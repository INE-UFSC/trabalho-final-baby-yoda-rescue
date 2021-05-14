from abc import ABC, abstractmethod


class abstest(ABC):
    def __init__(self):
        self.__std_test = "TESTE"

    @ property
    def std_test(self):
        return self.__std_test
