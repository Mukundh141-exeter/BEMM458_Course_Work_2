import numpy as np
import pandas as pd
from FREDMD_Tools import *

backtest_dates = pd.date_range(start='2005-1-1',end='2021-3-1',freq='M').to_period('M')
horizons=[3,6,9,12]

#add your code here: