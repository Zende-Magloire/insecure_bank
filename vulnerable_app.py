from flask import Flask, request, render_template

app = Flask(__name__)

class Account:
    def __init__(self, username: str):
        self.User: str = username
        self.Currency: str = '$'
        self.Balance: float = 1000

    def Update_Balance(self, money: float):
        self.Balance = money

    def Withdraw(self, amount: float):
        if amount <= self.Balance:
            money = self.Balance - amount
            self.Update_Balance(money)
            return money
        return 0

def GetUserBySession():
    return Account('Dr. Plante')

user = GetUserBySession()

@app.route('/')
def index():
    paramURL = request.args
    withdraw_msg = ''
    try:
        withdrawAmount = float(paramURL.get('amount'))
        if withdrawAmount is not None:
            user.Withdraw(withdrawAmount)
            withdraw_msg = f'You withdrew {user.Currency} {str(withdrawAmount)}!'
    except:
        pass

    return render_template('withdraw.html',
                           username=user.User,
                           balance=str(user.Balance),
                           currency=user.Currency,
                           message=withdraw_msg)


if __name__ == '__main__':
    app.run(debug=True)
