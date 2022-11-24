import ast
import json

def classname(cls):
    return cls.__class__.__name__

def attr(name):
    return f'@{name}'

def ast_span(fields, node):
    span = f'{node.first_token.startpos}-{node.last_token.endpos}'
    return dict(fields, **{'@span': span})

def jsonify_ast(node, level=0):
    fields = {}
    for k in node._fields:
        value = getattr(node, k)
        if isinstance(value, ast.AST):
            if value._fields:
                fields[k] = jsonify_ast(value)
            else:
                fields[attr(k)] = classname(value)
        elif isinstance(value, list) and value:
            fields[k] = list(map(jsonify_ast, value))
        elif isinstance(value, (str, int, float)):
            fields[attr(k)] = value
    return {
        classname(node): ast_span(fields, node)
    }

def make_ast(code):
    tree = ast.parse(code)
    return jsonify_ast(tree)


print(json.dumps(jsonify_ast(atok.tree), indent=2))
