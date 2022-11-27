from typing import Optional, Union


class Locator:
    def __init__(self, parent: Optional['Locator'] = None) -> None:
        self._parent = parent
        self._expr = ''

    def call(self, func_name: str) -> 'Locator':
        self._expr = f'//Call[func/Name[@id="{func_name}"]]'
        return Locator(self)

    def arg(self, arg_name: Union[int, str]) -> 'Locator':
        self._expr = '//' + (
            self._kwarg_value(arg_name)
            if isinstance(arg_name, str)
            else self._arg_value(arg_name)
        )
        return Locator(self)

    @property
    def value(self) -> 'Locator':
        self._expr = '/value'
        return Locator(self)

    @property
    def full_xpath(self) -> 'str':
        return (
            self._parent.full_xpath
            if self._parent
            else ''
        ) + (self._expr or '//@span')

    def _arg_value(self, arg_pos: int) -> str:
        return f'args[{arg_pos+1}]'

    def _kwarg_value(self, arg_name: str) -> str:
        return f'keyword[@arg="{arg_name}"]'
