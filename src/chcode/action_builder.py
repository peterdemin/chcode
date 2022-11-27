from dataclasses import dataclass
import enum
from chcode.locator import Locator
from chcode.tree import Tree


class ActionType(enum.Enum):
    REPLACE = 'replace'


@dataclass
class Action:
    span: str


@dataclass
class ReplaceAction(Action):
    text: str

    def run(self, source: str) -> str:
        start, _, end = self.span.partition('-')
        return source[: int(start)] + self.text + source[int(end):]


class ActionBuilder:
    def __init__(self,
                 tree: Tree,
                 session: list) -> None:
        self._tree = tree
        self._session = session

    def replace(self, locator: Locator, text: str) -> 'ActionBuilder':
        self._session.append(
            ReplaceAction(
                span=self._tree.locate_first(locator),
                text=repr(text),
            )
        )
