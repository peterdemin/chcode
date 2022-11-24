import ast
from typing import Type

import asttokens


class ASTLoader:

    def __call__(self, source: str) -> dict:
        return self._jsonify_ast(asttokens.ASTTokens(source, parse=True).tree)

    def _jsonify_ast(self, node: ast.AST) -> dict:
        fields = {}
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
    def _classname(klass: Type) -> str:
        return klass.__class__.__name__

    @staticmethod
    def _attr(name: str) -> str:
        return f'@{name}'

    @staticmethod
    def _span(fields: dict, node: ast.AST) -> dict:
        if getattr(node, 'first_token', None):
            span = f'{node.first_token.startpos}-{node.last_token.endpos}'
            return dict(fields, **{'@span': span})
        return fields
