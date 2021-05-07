class TargetInvestment:
    """
    用于计算目标收益所需时间和目标时间收益值

    Args:
        goal----目标收益
        month----定存月数
        return_investment----年化收益率
        amount_investment----每月定存金额

    Returns:
        包含收益金额和时间的字符串
    """

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

