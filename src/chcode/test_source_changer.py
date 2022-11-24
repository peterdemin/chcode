from chcode.source_changer_factory import build_source_changer


def test_change_arg_value():
    source = 'setup(name="__TARGET__".format(x=123))'
    source_changer = build_source_changer(source)
    assert source_changer.arg_value('setup', 'name', 'chcode') == "setup(name='chcode')"
