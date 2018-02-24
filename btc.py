import random
import pandas as pd
import numpy as np
from scipy.stats import norm


btc = pd.DataFrame(pd.read_csv("btcprices.csv"))
btcReturns = [np.log(btc.Close[i]/btc.Close[i+1]) for i in range(730)]
btcPrices = list(btc.Close[:1460])[::-1]
btcStd = np.std(btcReturns, ddof=1)
btcAvg = np.average(btcReturns)
btcVar = btcStd**2
drift = btcAvg - (btcVar/2)
over20k, over30k, over40k = [], [], []
numbOfSims = 500
endPrice = 0
print("\n* * * * * * * * * * * * * * * * * *\nNumber of Simulations: ", numbOfSims)
for simulation in range(numbOfSims):
    btcPred = [btcPrices[-1]]
    for day in range(366):
        btcPred.append(btcPred[-1]*np.exp(drift+btcStd *
                                          norm.ppf(random.SystemRandom.random(0))))
    over20k.append((0 if btcPred[-1] <= 20000 else 1))
    over30k.append((0 if btcPred[-1] <= 30000 else 1))
    over40k.append((0 if btcPred[-1] <= 40000 else 1))
    endPrice += btcPred[-1]

prob20k, prob30k, prob40k = (over20k.count(
    1)/numbOfSims), (over30k.count(1)/numbOfSims), (over40k.count(1)/numbOfSims)
print(
    "Average predicted price of BTC on 11/26/2018: ${:.2f}".format(endPrice/numbOfSims))
print("Probability that BTC is over $20K by 11/26/2018: {}\nProbability that BTC is over $30K by 11/26/2018: {}\nProbability that BTC is over $40K by 11/26/2018: {}\n"
      .format(prob20k, prob30k, prob40k))
print("* * * * * * * * * * * * * * * * * *")
