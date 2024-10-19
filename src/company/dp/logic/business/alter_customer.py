from company.dp.logic.business import filter_customer


def alter_customer() -> str:
    x = filter_customer(10)
    return x
