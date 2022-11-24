from typing import Any, Union
import lxml.etree

from chcode.expr_builder import ExprBuilder
from chcode.loader import ASTLoader
from chcode.tree_converter import TreeConverter


class SourceChanger:
    def __init__(
        self,
        source: str,
        loader: ASTLoader,
        tree_converter: TreeConverter,
        expr_builder: ExprBuilder,
    ) -> None:
        self._source = source
        self._loader = loader
        self._tree_converter = tree_converter
        self._expr_builder = expr_builder

    def arg_value(self, func: str, arg_name: Union[int, str], value: Any) -> str:
        return self._sub_span(
            self._first_xpath(
                self._expr_builder.find_arg_value(func, arg_name),
            ),
            repr(value),
        )

    def _sub_span(self, span: str, sub: str) -> str:
        start, _, end = span.partition('-')
        return self._source[: int(start)] + sub + self._source[int(end):]

    @property
    def _tree(self) -> lxml.etree.ElementTree:
        return self._tree_converter(self._loader(self._source))

    def _first_xpath(self, expr: str) -> str:
        return self._tree.xpath(expr)[0]
