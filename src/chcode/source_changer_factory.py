from chcode.expr_builder import ExprBuilder
from chcode.loader import ASTLoader
from chcode.tree_converter import TreeConverter
from chcode.source_changer import SourceChanger


def build_source_changer(source: str) -> SourceChanger:
    return SourceChanger(
        source=source,
        loader=ASTLoader(),
        tree_converter=TreeConverter(),
        expr_builder=ExprBuilder(),
    )
