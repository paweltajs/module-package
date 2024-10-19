from company.dp.logic.business import review_customers


def test_review_customers():
    x = review_customers()
    assert x == "custom"
