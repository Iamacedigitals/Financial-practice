import numpy as np
import datetime as dt
import pandas as pd

class Portfolio:
    summary = ''
    
    def __init__(self):
        self.balance = 0
        self.history = [] # other lists will be appended so it can form a proper record with pd.Df
        self.investment_price_list = {
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
        } # Fetches all the correct information on the instrument from a specified websocket or hard coded list.
        self.holdings = {} # Follows a format of "name of instrument":no of holdings, the name of the instrument and holdings are filled in to by the position class
        self.investment_weights = {} # Follow a format of "name of instrument": weight on the portfolio (Initially without rebalancing)
        self.leverage = []
        self.asset_information = {}
        self.open_positions = dict()

    def get_instrument_price(self, asset_name: str|list) :
        asset_prices = {}
        if type(asset_name) == str:
            if asset_name in self.investment_price_list:
                asset_prices.update({asset_name : [self.investment_price_list[asset_name]]})
                return asset_prices
            else:
                print("This instrument is not on your watchlist, recheck name or add the instrument")
                asset_name = input(f"""
                                   Re-enter name of the instrument, 
                                   Available Instrumnets include 
                                   {list(self.investment_price_list.keys())}:

                                   >> """)
                if asset_name in self.investment_price_list:
                    asset_prices.update({asset_name : [self.investment_price_list[asset_name]]})
                    return asset_prices
                else:
                    self.get_instrument_price(asset_name)
                    return asset_prices
        elif type(asset_name) == list:
            for name in asset_name:
                if name in self.investment_price_list:
                    asset_prices.update({name : [self.investment_price_list[name]]})
                else:
                    print(f"{name} instrument is not on your watchlist, recheck name or add the instrument")
                    print(f"""
                    Available Instrumnets include 
                    {list(self.investment_price_list.keys())}
""")                                    
                    reset_asset_name = input(f"""
                                   Re-enter name of the instrument, 
                                   Available Instrumnets include 
                                   {list(self.investment_price_list.keys())}:

                                   >> """)
                    if reset_asset_name in self.investment_price_list:
                        asset_prices.update({reset_asset_name : [self.investment_price_list[reset_asset_name]]})
                    else:
                        new_price = self.get_instrument_price([reset_asset_name])
                        asset_prices.update({reset_asset_name: [new_price[0]]})
                    continue
            return asset_prices
    def add_position(self, assets: str|list):
        get_price = self.get_instrument_price(assets)
        if type(assets) == list:
            for asset in assets:
                holdings_per_asset = int(
                    input(f"""
How many {asset}s do you want to buy """)
)
                leverage = int(input("How much leverage: "))
                if asset in self.holdings:
                    self.holdings[asset] += holdings_per_asset
                    self.asset_information[asset][1] = self.holdings[asset]
                else:
                    self.holdings.update({
                        asset: holdings_per_asset
                        })
                    self.leverage.append(leverage)
                    self.asset_information.update({
                        asset : get_price[asset]
                    })
                    self.asset_information[asset].append(self.holdings[asset])
                    self.asset_information[asset].append(leverage)
                    print(self.asset_information)
            position_info = pd.DataFrame(self.asset_information).T
            position_info.columns = ["Entry Price","Holdings", "Leverage" ]
            position_info["Investment Value"] = position_info["Holdings"] * position_info["Entry Price"]
            position_info["Margin value"] =  position_info["Investment Value"] / np.array(self.leverage)
            position_info.to_csv("Investment Postions.csv")
            self.open_positions = position_info
            return self.open_positions
        else:
            get_price = self.get_instrument_price(assets)
            holdings_per_asset = int(
                input(f"""
How many {assets}s do you want to buy """))
            leverage = int(input("How much leverage: "))
            if assets in self.holdings:
                    self.holdings[assets] += holdings_per_asset
                    self.asset_information[assets][1] = self.holdings[assets]
            else:
                self.holdings.update({
                    assets: holdings_per_asset
                    })
                self.leverage.append(leverage)
                self.asset_information.update({
                    assets : get_price[assets]
                })
                self.asset_information[assets].append(self.holdings[assets])
                self.asset_information[assets].append(leverage)
                print(self.asset_information)
            position_info = pd.DataFrame(self.asset_information).T
            position_info.columns = ["Entry Price","Holdings", "Leverage" ]
            position_info["Investment Value"] = position_info["Holdings"] * position_info["Entry Price"]
            position_info["Margin Value"] =  position_info["Investment Value"] / np.array(self.leverage)
            position_info.to_csv("Investment Postions.csv")
            self.open_positions = position_info
            return self.open_positions
    def remove_position(self, assets: str|list) -> str|list:
        pass

David  = Portfolio()
print(David.add_position("Gold"))
# print(David.add_position(["Bitcoin"]))
# print(David.add_position(["Bitcoin"]))
# # print(David.add_position(["Bitcoin"]))