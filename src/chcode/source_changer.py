from typing import Any, Union, List

from chcode.locator import Locator
from chcode.action_builder import ActionBuilder, Action
from chcode.tree import TreeBuilder


class SourceChanger:
    def __init__(
        self,
        source: str,
        tree_builder: TreeBuilder,
    ) -> None:
        self._source = source
        self._tree_builder = tree_builder

    def arg_value(self, func: str, arg_name: Union[int, str], value: Any) -> str:
        session: List[Action] = []
        ActionBuilder(
            tree=self._tree_builder(self._source),
            session=session
        ).replace(
            Locator().call(func).arg(arg_name).value,
            value,
        )
        source = self._source
        for action in session:
            source = action.run(self._source)
        return source
