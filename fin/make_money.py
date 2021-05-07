class TargetInvestment:
    def __init__(self):
        self.goal = 1000000
        self.month = 12
        self.return_investment = 0.12
        self.amount_investment = 10000

    @staticmethod
    def achieved_time(goal, return_investment, amount_investment):
        total_investment = 0
        months_investment = 0
        while total_investment - goal < 0:
            total_investment = total_investment * (1 + float(return_investment) / 12.0) + amount_investment
            months_investment += 1

        return "You have invested {months_investment} months, " \
               "it's {year_investment} years " \
               "and you got {total_investment} YUAN!".format(months_investment=months_investment,
                                                             year_investment=int(months_investment / 12.0),
                                                             total_investment=total_investment)

    @staticmethod
    def achieved_money(month, return_investment, amount_investment):
        total_investment = 0
        for i in range(month):
            total_investment = total_investment * (1 + float(return_investment) / 12.0) + amount_investment

        return "You want invested {months_investment} months, " \
               "it's {year_investment} years " \
               "and you got {total_investment} YUAN!".format(months_investment=month,
                                                             year_investment=int(month / 12.0),
                                                             total_investment=total_investment)

