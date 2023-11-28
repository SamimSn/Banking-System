from project import Bank_Account, date, deposit, calculate_years, create_acc

def test_deposit():
    acc = Bank_Account(20, "Samim", date(2000, 12, 25), "Gorgan", 60)
    deposit(acc, 20)
    assert acc._balance == 80

def test_calculate_years():
    acc = Bank_Account(22, "Jack", date(1999, 1, 1), "Shiraz", 120)
    assert calculate_years(acc) == 24

def test_create_acc():
    acc_1 = Bank_Account(32, "Alex", date(2015, 1, 2), "LA", 550)
    acc_2 = create_acc(32, "Alex", date(2015, 1, 2), "LA", 550)
    assert acc_1._id == acc_2._id
    assert acc_1._name == acc_2._name
    assert acc_1._birth_date == acc_2._birth_date
    assert acc_1._city == acc_2._city
    assert acc_1._balance == acc_2._balance
