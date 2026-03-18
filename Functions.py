import numpy as np
import pandas as pd

class InvestorProfile:
    def __init__(self, holdings:int|list, instruments: str|list, risks, speculations, investment_price_list: dict):
        self.holdings = holdings
        self.instruments = instruments # This one is for all the currently available investments 
        self.risks = risks
        self.speculations = speculations
        self.returns = []
        self.investment_price_list = investment_price_list # this is is just a price list. and it is updated with new postions that are added 
class Portfolio(InvestorProfile):
    def __init__(self, holdings, instruments, risks, speculations, investment_price_list):
        super().__init__(holdings, instruments, risks, speculations, investment_price_list)
        self.value = 0
        self.investmets =  list() # name of assest, and values of invested amounts "Apple": 50usd, the investements are holdings * price, sum(holdings * price)
        self.positions = dict() # namme of all open postions A
        self.weight = None
        self.price = None

    def get_instrument_price(self, asset_name: str|list) :
        if type(asset_name) == str:
            if asset_name in self.investment_price_list:
                self.price = self.investment_price_list[asset_name]
                return self.price
            else:
                print("This instrument is not on your watchlist, recheck name or add the instrument")
                asset_name = input(f"""
                                   Re-enter name of the instrument, 
                                   Available Instrumnets include 
                                   {list(self.investment_price_list.keys())}:

                                   >> """)
                if asset_name in self.investment_price_list:
                    self.price = self.investment_price_list[asset_name]
                    return self.price
                else:
                    self.get_instrument_price(asset_name)
                    return self.price
        elif type(asset_name) == list:
            asset_prices = []
            for name in asset_name:
                if name in self.investment_price_list:
                    asset_prices.append(self.investment_price_list[name])
                else:
                    print(f"{name} instrument is not on your watchlist, recheck name or add the instrument")
                    print(f"""
                    Available Instrumnets include 
                    {list(self.investment_price_list.keys())}
""")
                    asset_prices.append(None)
                    continue
            self.price = asset_prices
            return self.price
    def calc_portfolio_value(self):
        price  = np.array(self.get_instrument_price(self.instruments))
        holdings =  np.array(self.holdings)
        value = np.sum(price * holdings)
        return value
        # pass
        # initial_value = np.array(self.holdings) * np.array(instruments_price)
        
    def add_position(self, name:str|list, holdings:float|int|list, price:int): #, name:str|list, holdings:float|int
        if (type(name) == list) & (type(holdings) == list):
            for i,value in enumerate(name):
                self.positions[value]= holdings[i]
                self.investment_price_list[value] = price
                self.holdings.append[holdings[i]]
            return self.positions
        else:
            self.investment_price_list[value] = price
            self.positions.update({
                name:holdings
            })
            self.investment_price_list.update({
                name:price
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
risks = [0.1, 0.2, 0.3] 
speculations = ["Tesla", "Nvidia", "Sugar", "Cattle", "Silver"]

investment_price_list = {
    "Bitcoin": 70000,
    "Gold": 5100,
    "Apple": 300, 
    "Microsoft": 291, 
    "Oil": 50,
    "Tesla": 321, 
    "Nvidia":435, 
    "Sugar":20, 
    "Cattle":400, 
    "Silver":75
}

Investor = InvestorProfile(holdings, instruments, risks, speculations, investment_price_list)
InvestorPortfolio = Portfolio(Investor.holdings,Investor.instruments, Investor.risks, Investor.speculations, Investor.investment_price_list)
# print(InvestorPortfolio.add_position("Solana", 40, 120))
print(InvestorPortfolio.positions)
print(InvestorPortfolio.calc_portfolio_value())
# print(InvestorPortfolio.__dict__)

for asset in assets:
            holdings += int(input(f"""
How many {asset}s do you want to buy """))
            leverage = int(input("How much leverage: ")) 
            if asset not in self.open_positions:
                asset_information[asset].append(holdings)
                asset_information[asset].append(leverage)
                position_info = pd.DataFrame(asset_information).T
            elif asset in position_info:
                position_info.loc[asset, "Holdings"] += holdings   
        position_info.columns = ["Entry Price", "Holdings", "Leverage"]
        def position_value():       
            return position_info["Holdings"] * position_info["Entry Price"]
        position_info["Value"] = position_value()
        return position_info