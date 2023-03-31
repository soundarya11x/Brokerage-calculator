import streamlit as st
trade_type = st.selectbox(
    'Select Trade Type',
    ('Delivery equity',' Intraday equity', 'F&O - Futures','F&O - Options'))
exchange = st.radio(
    "Select Exchange",
    ("NSE","BSE"))
buy =  float(st.number_input('Buy'))
sell =  float(st.number_input('Sell'))
quantity = int(st.number_input('Quantity'))
company = st.selectbox(
	'Select a Stock Broker',
	('Zerodha','Groww','Angel','Upstox'))

change = (sell - buy) * quantity
if sell > buy :
	p_or_l = "PROFIT" 
	
else:
	p_or_l = "LOSS"


turnover = (buy + sell) * quantity
profit_or_loss = st.metric(label = p_or_l, value = change, delta = change)

t_ovr = st.metric(label = "Turnover",value = turnover)

def get_rates():
    return {"ZERODHA": {"Brokerage": [0, 20, 20, 20],
                        "STT": [ 0.1,0.025, 0.01, 0.05],
                        "ExchTrnChrg": {"NSE" : [0.00345, 0.00345, 0.002, 0.053], "BSE" : [0.00375,0.00375,0,0]} ,
                        "ClearingChrg": [0, 0, 0, 0],
                        "SEBIChrg": [0.0001, 0.0001, 0.0001, 0.0001],
                        "StampDuty": [ 0.015,0.003,0.002, 0.003],
                        },
            "ANGEL": {"Brokerage": [40, 0, 40, 40],
                      "STT": [0.025, 0.1, 0.01, 0.05],
                      "ExchTrnChrg": [0.00345, 0.00345, 0.002, 0.053],
                      "ClearingChrg": [0, 0, 0, 0],
                      "SEBIChrg": [0.0001, 0.0001, 0.0001, 0.0001],
                      "StampDuty": [0.003, 0.015, 0.002, 0.003],
                      },
            "UPSTOX": {"Brokerage": [40, 0, 40, 40],
                       "STT": [0.025, 0.1, 0.01, 0.05],
                       "ExchTrnChrg": [0.00345, 0.00345, 0.002, 0.053],
                       "ClearingChrg": [0, 0, 0, 0],
                       "SEBIChrg": [0.00005, 0.00005, 0.00005, 0.00005],
                       "StampDuty": [0.003, 0.015, 0.002, 0.003],
                       },
            "GROWW": {"Brokerage": [18, 0, 18, 0],
                       "STT": [0.025, 0.1, 0.1, 0.05],
                       "ExchTrnChrg": [0.00345, 0.00345, 0.002, 0.053],
                       "ClearingChrg": [0, 0, 0.016, 0.025],
                       "SEBIChrg": [0.0001, 0.0001, 0.0001, 0.0001],
                       "StampDuty": [0.003, 0.015, 0.002, 0.003],
                       },
        
            }

  
