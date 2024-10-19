from company.dp.logic.business import alter_customer


def test_alter_customer():
    x = alter_customer()
    assert x == 10
