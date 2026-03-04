class BankTerminal:

    def __init__(self, holder, balance, history=None):
        self.holder = holder
        self.balance = balance
        self.history = history if history is not None else []

    def add_money(self, amount):
        self.balance += amount
        self.history.append(f'+{amount} руб.: пополнение')
        print('Счет успешно пополнен')

    def get_report(self):
        self.balance -= 50
        self.history.append(f'-50 руб.: списание за выписку по карте')
        print(f'Ваш баланс: {self.balance}')
        print('История операций:')
        print('\n'.join(self.history))

    def take_loan(self, amount):
        self.balance += amount*0.8
        self.history.append(f'+{amount} руб.: пополнение за счет кредитных средств')
        self.history.append(f'-{amount*0.2} руб.: списание по кредиту')
        print('Ваш счет пополнен кредитными средствами')

    def transfer(self, other_account, amount):
        if self.balance >= amount*1.05:
            self.balance -= amount*1.05
            self.history.append(f'-{amount*1.05} руб.: перевод денежных средств другому лицу')
            other_account.add_money(amount)
            print(f'Перевод успешно выполнен, комиссия составила {amount*0.05} руб')
        else:
            print('Операция не выполнена, не хватает денежных средств')


acc1_name = input('Введите ваше имя: ')

acc1 = BankTerminal(acc1_name, 1000)
acc2 = BankTerminal("Иван", 0)
acc3 = BankTerminal("Петр", 0)

accounts = {'Иван': acc2, 'Петр': acc3}

while True:
    print(('Какие дейсndия вы хотите совершить с денежными средствами на вашем счете? '
           'Пополнить/получить выписку/получить кредит/выполнить перевод другому лицу?'
           'Если хотите завершить работу - введите "Конец"'))
    action = input().lower()
    if action == 'пополнить':
        amount_plus = int(input('Введите сумму пополнения: '))
        acc1.add_money(amount_plus)
    elif action == 'получить выписку':
        acc1.get_report()
    elif action == 'получить кредит':
        amount_credit = int(input('Введите сумму кредита: '))
        acc1.take_loan(amount_credit)
    elif action == 'выполнить перевод другому лицу':
        name_transfer = input('Кому из ваших контактов вы хотите сделать перевод (Иван/Петр): ')
        amount_transfer = int(input('Введите сумму перевода: '))
        acc1.transfer(accounts[name_transfer], amount_transfer)
    elif action == 'конец':
        print('До свидания, будем рады видеть Вас снова')
        break
    else:
        print('Введено неверное название операции. Пожалуйста, введите верное название операции из предложенных')
