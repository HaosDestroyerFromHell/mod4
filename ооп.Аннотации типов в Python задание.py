from typing import Union

class BankAccount:
    """
    Класс, представляющий работу баланса счета в банке
    """
    
    def __init__(self, account_number: int, balance: int | float):
        """
        Создание и подготовка к работе объекта класса BankAccount
        :param account_number: int: номер аккаунта
        :param balance: int | float: баланс счета
        """
        self._account_number = account_number
        self._balance = balance
        
    @property
    def balance(self) -> int | float:
        return self._balance
    
    def deposit(self, amount: int | float) -> None:
        """
        Зачисляет указанную сумму на баланс.

        param: amount: int | float: сумма, которую необходимо зачислить. 
                          должна быть положительным числом.

        ValueError: если сумма меньше или равна нулю, выводится сообщение о том, 
        что сумма должна быть положительной, и зачисление не происходит.

        >>> account = BankAccount(213213213, 1000)
        >>> account.deposit(-50)
        
        """
        if not isinstance(amount, (int, float)):
            raise ValueError('Ошибка ввода числа для зачисления средств')
        if amount > 0:
            self._balance += amount
        else:
            print('Cумма должна быть положительной')
    
    def withdraw(self, amount: int | float) -> None:
        """
        Списыввает указанную сумму денег.
        
        param: amount: int | float: сумма, которую нужно списать, должна быть положительной.
        
        raise: ValueError: если число больше нуля и меньше или равно балансу, то призойдет списание, 
        иначе выдаст ошибку.
    
        >>> account = BankAccount(213213213, 1000)
        >>> account.deposit(100)
        >>> account.withdraw(100000)
        
        """
        if not isinstance(amount, (int, float)):
            raise ValueError('Ошибка ввода числа для снятия средств')
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print('Недостаточно средств')
            
    def calculate_interest(self, rate: int | float) -> None:
        """
        принимает процент вклада, возвращает баланс с учетом процентов.
        param: rate: int | float: процент вклада
        raise: ValueError: если число меньше нуля или не соответствует тип данных, выдает ошибку.
        >>> account = BankAccount(213213213, 1000)
        >>> account.deposit(100)
        >>> account.calculate_interest(-10)    
        
        """
        if not isinstance(rate, (int, float)) or rate < 0:
            raise ValueError('Ошибка ввода')
        interest = self._balance / 100 * rate
        self._balance += interest
        print(f'Начислены проценты {round(interest)}, баланс с учетом процентов: {self.balance}')        
        
    @balance.setter
    def balance(self, value: Union[int, float]) -> None:
        """
        доступ к приватному атрибуту баланс.
        param: value: int | float: баланс вклада
        raise: ValueError: если число меньше нуля или не соответствует тип данных, выдает ошибку.
        >>> account = BankAccount(213213213, 1000)
        >>> account.balance = -1000
        >>> print(account)
        """
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Счет должен быть положительным.")
        self._balance = value
        
    
acc1 = BankAccount(123456789, 1000)
print(acc1.balance)

acc1.deposit(2133)
print("Баланс после внесения:", acc1.balance)

acc1.withdraw(100)
print("Баланс после снятия:", acc1.balance)

acc1.calculate_interest(10)
print('Баланс с учетом начисления процентов', acc1.balance)

#acc1.balance = -21312 # попытка установить отрицательно число на счёт
print(acc1)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()