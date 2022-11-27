from chcode.loader import ASTLoader
from chcode.source_changer import SourceChanger
from chcode.tree import TreeBuilder
from chcode.tree_converter import TreeConverter


def build_source_changer(source: str) -> SourceChanger:
    return SourceChanger(
        source=source,
        tree_builder=TreeBuilder(
            loader=ASTLoader(),
            tree_converter=TreeConverter(),
        ),
    )
