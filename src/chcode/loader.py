import ast
from typing import Any, Dict, Union

import asttokens


class ASTLoader:
    def __call__(self, source: str) -> dict:
        module = asttokens.ASTTokens(source, parse=True).tree
        assert module
        return self._jsonify_ast(module)

    def _jsonify_ast(self, node: Union[ast.Module, ast.AST]) -> dict:
        fields: Dict[str, Any] = {}
        for k in node._fields:
            value = getattr(node, k)
            if isinstance(value, ast.AST):
                if value._fields:
                    fields[k] = self._jsonify_ast(value)
                else:
                    fields[self._attr(k)] = self._classname(value)
            elif isinstance(value, list) and value:
                fields[k] = list(map(self._jsonify_ast, value))
            elif isinstance(value, (str, int, float)):
                fields[self._attr(k)] = value
        return {self._classname(node): self._span(fields, node)}

    @staticmethod
    def _classname(klass: Any) -> str:
        return klass.__class__.__name__

    @staticmethod
    def _attr(name: str) -> str:
        return f'@{name}'

    @staticmethod
    def _span(fields: dict, node: ast.AST) -> dict:
        if getattr(node, 'first_token', None):
            start = node.first_token.startpos  # type: ignore[attr-defined]
            end = node.last_token.endpos  # type: ignore[attr-defined]
            span = f'{start}-{end}'
            return dict(fields, **{'@span': span})
        return fields
