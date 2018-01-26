#!/usr/bin/env python
import sys, os
jp = os.path.join

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import seaborn as sb

DATADIR='data'
WEBDIR='www'

if __name__ == '__main__':
    df = pd.read_csv(jp('data', 'manfct80s.csv'), low_memory=False)
    print "Nrows %d, Ncols %d"%(df.shape[0], df.shape[1])
    
    ## get numeric columns
    descr_tbl = df.describe().transpose()
    
    for col in descr_tbl.index:
        ##if descr_tbl.loc[col]['count']>0:
        try:
            print "plotting col %s"%(col)
            fig = plt.figure(figsize=(12,8))
            plt.hist(df[col])
            plt.title("%s"%(col))
            fig.savefig(jp(WEBDIR, "hist_%s.png"%(col)))
            ##else:
        except:
            print "skipping col %s"%(col)
            
