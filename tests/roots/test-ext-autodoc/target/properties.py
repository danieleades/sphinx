class Foo:
    """docstring"""

    @property
    def prop1(self) -> int:
        """docstring"""

    @classmethod
    @property
    def prop2(cls) -> int:
        """docstring"""

    @property
    def prop1_with_type_comment(self):
        # type: () -> int
        """docstring"""

    @classmethod
    @property
    def prop2_with_type_comment(cls):
        # type: () -> int
        """docstring"""
