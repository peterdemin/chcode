import json
import asttokens, ast
import xmltodict
import lxml


def span_text(source, span):
    start, _, end = span.partition('-')
    return source[int(start): int(end)]


def sub_span(source, span, sub):
    start, _, end = span.partition('-')
    return source[:int(start)] + sub + source[int(end):]


source = '''
setup(
    name="__TARGET__".format(x=123),
)
'''
tree = lxml.etree.fromstring(xmltodict.unparse(jsonify_ast(asttokens.ASTTokens(source, parse=True).tree)).encode('utf-8'))
elem = tree.xpath('//*[@value="__TARGET__"]')[0]


def change_arg_value(source, func, kwarg, value):
    tree = lxml.etree.fromstring(xmltodict.unparse(jsonify_ast(asttokens.ASTTokens(source, parse=True).tree)).encode('utf-8'))
    expr = tree.xpath(f'//Call[func/Name[@id="{func}"]]//keyword[@arg="{kwarg}"]/value//@span')
    return sub_span(source, expr[0], repr(value))


def main() -> None:
    pass


if __name__ == '__main__':
    main()
