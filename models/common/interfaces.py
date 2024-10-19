import abc


class IdGenerator(abc.ABC):
    """Id generator interface"""

    @abc.abstractmethod
    def generate(self) -> str:
        """Generate uuid"""
