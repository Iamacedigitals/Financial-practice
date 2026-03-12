class InvestorProfile:
    def __init__(self, holdings, instruments, risks, speculations):
        self.holdings = holdings
        self.instruments = instruments
        self.risks = risks
        self.speculations = speculations
        self.returns = []
class Portfolio(InvestorProfile):
    def __init__(self, holdings, instruments, risks, speculations):
        super().__init__(holdings, instruments, risks, speculations)
        self.value = 0
        self.investmets =  list() # name of assest, and values of invested amounts "Apple": 50usd
        self.positions = dict() # namme of assets and values of holdings, "Apple": 20 units
        self.weight = None
        self.price = None
    def print_retutrns(self):
        return self.returns
    def calc_portfolio_value(self):
        return self.value
    def add_position(self, name:str|list, holdings:float|int|list): #, name:str|list, holdings:float|int
        if (type(name) == list) & (type(holdings) == list):
            for i,value in enumerate(name):
                self.positions[value]= holdings[i]
            return self.positions
        else:
            self.positions.update({
                name:holdings
            })
            return self.positions
    def calc_returns():
        pass
    def __repr__(self):
        return f"This is the Portfolio class in progress"
    
# portfolio.calc_portfolio_value()
# print(portfolio.add_position(name = ["Apple", "BTC"],holdings= [70, 50]))

holdings = [20, 45, 35, 10, 12]
instruments = ["Apple", "Microsoft", "Oil", "Gold", "Bitcoin"]
risks = [0.1, 0.2, 0.3, 0.4, 0.5]
speculations = ["Tesla", "Nvidia", "Sugar", "Cattle", "Silver"]
Investor = InvestorProfile(holdings, instruments, risks, speculations)
InvestorPortfolio = Portfolio(Investor.holdings,Investor.instruments, Investor.risks, Investor.speculations)

print(InvestorPortfolio.print_retutrns())

Investor2 = InvestorProfile(holdings=15, instruments="Dangote Group", risks=0.1, speculations="Samsung")
print(Investor2.holdings)