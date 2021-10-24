# Imports you may need
import seaborn as sns
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import numpy as np
import json
import bz2
from dataloader import *

def section1a(df):
    print("We can first plot the distribution of the publication date")
    df = df['date']
    pd.to_datetime(df).hist()
    plt.show()
    
    print("Then make it in red")
    pd.to_datetime(df).hist(color="red")
    plt.show()
    