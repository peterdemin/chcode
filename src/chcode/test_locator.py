from chcode.locator import Locator


def test_func_arg_value():
    result = Locator().call('setup').arg('name').value.full_xpath
    assert result == '//Call[func/Name[@id="setup"]]//keyword[@arg="name"]/value//@span'
