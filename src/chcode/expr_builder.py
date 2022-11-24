from typing import Union


class ExprBuilder:
    def find_arg_value(self, func_name: str, arg_name: Union[int, str]) -> str:
        value_locator = (
            self._kwarg_value(arg_name)
            if isinstance(arg_name, str)
            else self._arg_value(arg_name)
        )
        return '//'.join((
            '',
            self._func_call(func_name),
            value_locator,
            self._span(),
        ))

    def _func_call(self, func_name: str) -> str:
        return f'Call[func/Name[@id="{func_name}"]]'

    def _arg_value(self, arg_pos: int) -> str:
        return f'args/*[position()={arg_pos}]'

    def _kwarg_value(self, arg_name: str) -> str:
        return f'keyword[@arg="{arg_name}"]/value'

    def _span(self) -> str:
        return '@span'
