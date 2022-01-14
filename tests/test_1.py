from pytest import mark


ddt = {
    'argnames': 'name, description',
    'argvalues': [
                    ('hello', 'world'),
                    ('zzzzz', ''),
                    ('123', 'world'),
                ],
    'ids': ['general test', 'test with no discription', 'test with digits'],
}


@mark.parametrize(**ddt)
def test_added_new_test_case(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)


def test_testcase_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to('Test Cases')
    assert not desktop_app_auth.test_cases.check_test_exists('djdjddjdjdj')
