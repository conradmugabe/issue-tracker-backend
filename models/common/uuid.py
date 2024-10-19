from uuid import uuid4 as uuid
from .interfaces import IdGenerator


class UUIDGenerator(IdGenerator):
    """UUID generator"""

    def generate(self) -> str:
        """Generate uuid"""
        return str(uuid())
