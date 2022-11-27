import lxml.etree
from chcode.locator import Locator
from chcode.tree_converter import TreeConverter
from chcode.loader import ASTLoader


class Tree:
    def __init__(self, xml_tree: lxml.etree.ElementTree) -> None:
        self._xml_tree = xml_tree

    def locate_first(self, locator: Locator) -> str:
        expr = locator.full_xpath
        try:
            return self._xml_tree.xpath(expr)[0]
        except lxml.etree.XPathEvalError as exc:
            raise ValueError(expr) from exc


class TreeBuilder:
    def __init__(
        self,
        loader: ASTLoader,
        tree_converter: TreeConverter,
    ) -> None:
        self._loader = loader
        self._tree_converter = tree_converter

    def __call__(self, source) -> Tree:
        return Tree(self._tree_converter(self._loader(source)))
