from abc import abstractmethod, ABC


class Supply(ABC):

    @abstractmethod
    def __init__(self, needs_increase):
        self.__needs_increase = needs_increase # Private attribute

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase = value

    def apply(self, survivor):
        survivor.needs += self.needs_increase