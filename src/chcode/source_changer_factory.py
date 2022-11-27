from chcode.loader import ASTLoader
from chcode.tree_converter import TreeConverter
from chcode.source_changer import SourceChanger
from chcode.tree import TreeBuilder


def build_source_changer(source: str) -> SourceChanger:
    return SourceChanger(
        source=source,
        tree_builder=TreeBuilder(
            loader=ASTLoader(),
            tree_converter=TreeConverter(),
        )
    )
