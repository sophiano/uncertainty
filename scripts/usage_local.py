# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:51:19 2021

@author: sopmathieu

This script is an example of how to use to package to study the sunspot 
numbers. 

"""

import pickle
import numpy as np 
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14
import sys
sys.path.insert(1, '/uncertainty/')

from uncertainty import errors as err

### load data (loaded automatically with package)
with open('data/data_21_1947', 'rb') as file: #subset of 21 stations
#with open(data_path + '/data_1981', 'rb') as file: #all stations
     my_depickler = pickle.Unpickler(file)
     Ns = my_depickler.load() #number of spots
     Ng = my_depickler.load() #number of sunspot groups
     Nc = my_depickler.load() #Ns+10Ng
     station_names = my_depickler.load() #index of the stations
     time = my_depickler.load() #time (fraction of years)
     
Ns_rescaled = err.rescaling(Ns, 8)    

####################################    
### Solar signal

mus_Ns = err.median_transformed(Ns, period_rescaling=8)
mus_Ng = err.median_transformed(Ng, period_rescaling=14)
mus_Nc = err.median_transformed(Nc, period_rescaling=10)

### histograms
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.figure(1)  
plt.hist(mus_Ns[~np.isnan(mus_Ns)], range=[0,150], bins='auto', density=True, facecolor='b')  
plt.title("Solar signal (Ns)")
plt.text(60, 0.04, 'mean: ' '%4f' %np.nanmean(mus_Ns))
plt.text(60, 0.03, 'std: ' '%4f' %np.nanstd(mus_Ns))
plt.axis([0,150, 0, 0.08])
plt.grid(True)
plt.show()

plt.figure(2)  
plt.hist(mus_Ng[~np.isnan(mus_Ng)], range=[0,20], bins=20, density=True, facecolor='b')  
plt.title("Solar signal (Ng)")
plt.text(15, 0.2, 'mean: ' '%4f' %np.nanmean(mus_Ng))
plt.text(15, 0.15, 'std: ' '%4f' %np.nanstd(mus_Ng))
plt.axis([0, 20, 0, 0.25])
plt.grid(True)
plt.show()

plt.figure(3)  
plt.hist(mus_Nc[~np.isnan(mus_Nc)], range=[0,300], bins='auto', density=True, facecolor='b')  
plt.title("Solat signal (Nc)")
plt.text(150, 0.015, 'mean: ' '%4f' %np.nanmean(mus_Nc))
plt.text(150, 0.0125, 'std: ' '%4f' %np.nanstd(mus_Nc))
plt.axis([0, 300, 0, 0.03])
plt.grid(True)
plt.show()


####################################    
### Long-term error 

mu2_81 = err.long_term_error(Ns, period_rescaling=8, wdw=81)
mu2_1 = err.long_term_error(Ns, period_rescaling=8, wdw=365)
mu2_2 = err.long_term_error(Ns, period_rescaling=8, wdw=912)

#stability criterion
#mse_mu2, names = err.mse_criterion(mu2_1, station_names, ref=None)
mse_mu2, names = err.mse_criterion(mu2_1, station_names, ref=1)

plt.rcParams['figure.figsize'] = (10.0, 6.0)
start = np.where(time == 1960)[0][0]
stop = np.where(time == 2010)[0][0]
stat = 19
fig = plt.figure()
plt.plot(time[start:stop], mu2_81[start:stop, stat], ':', c='tab:green', label='$\hat \mu_2$ (81)')
plt.plot(time[start:stop], mu2_1[start:stop, stat], '--', c='tab:red', label='$\hat \mu_2$ (1)')
plt.plot(time[start:stop], mu2_2[start:stop, stat], lw=3, c='tab:blue', label='$\hat \mu_2$ (2)')
plt.plot([time[start], time[stop]], [1, 1], 'k-', lw=2)
plt.legend(loc='upper right')
#f4.set_ylim([-10,20]); f4.set_xlim([time[start-20], time[stop+20]])
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 10)
plt.xticks(x_ticks)
plt.title("Long-term error for Ns in %s" %station_names[stat])
plt.ylabel('$\hat \mu_2$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
#fig.savefig('mu2_Ns_SM.pdf')
plt.show()


####################################
### Error at minima

e3_Ns = err.error_at_minima(Ns, period_rescaling=8)
e3_Ng = err.error_at_minima(Ng, period_rescaling=14)
e3_Nc = err.error_at_minima(Nc, period_rescaling=10)

### histograms
binning = int(6/(3.5*np.nanstd(e3_Ns)*len(e3_Ns)**(-1/3))) #Scott's rule
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.figure(1)  
plt.hist(e3_Ns[~np.isnan(e3_Ns)], range=[0,5], bins=binning, density=True, facecolor='b')  
plt.title("Error at minima (Ns)")
plt.text(2, 0.8, 'mean:' '%4f' %np.nanmean(e3_Ns))
plt.text(2, 0.6, 'std:' '%4f' %np.nanstd(e3_Ns))
plt.axis([0, 5, 0, 1])
plt.grid(True)
plt.show()

binning = int(6/(3.5*np.nanstd(e3_Ng)*len(e3_Ng)**(-1/3)))
plt.figure(2)  
plt.hist(e3_Ng[~np.isnan(e3_Ng)], range=[0,5], bins=binning, density=True, facecolor='b')  
plt.title("Error at minima (Ng)")
plt.text(2, 0.8, 'mean:' '%4f' %np.nanmean(e3_Ng))
plt.text(2, 0.6, 'std:' '%4f' %np.nanstd(e3_Ng))
plt.axis([0, 5, 0, 1])
plt.grid(True)
plt.show()

binning = int(6/(3.5*np.nanstd(e3_Nc)*len(e3_Nc)**(-1/3)))
plt.figure(3)  
plt.hist(e3_Nc[~np.isnan(e3_Nc)], range=[0,30], bins=binning, density=True, facecolor='b')  
plt.title("Error at minima (Nc)")
plt.text(10, 0.03, 'mean:' '%4f' %np.nanmean(e3_Nc))
plt.text(10, 0.02, 'std:' '%4f' %np.nanstd(e3_Nc))
plt.axis([0, 30, 0, 0.04])
plt.grid(True)
plt.show()

##################
### Short-term error

e1_Ns = err.short_term_error(Ns, period_rescaling=8)
e1_Ng = err.short_term_error(Ng, period_rescaling=14)
e1_Nc = err.short_term_error(Nc, period_rescaling=10)

#stability criterion
#mse_e1, names = err.mse_criterion(e1_Ns, station_names, ref=None)
mse_e1, names = err.mse_criterion(e1_Ns, station_names, ref=1)

###histograms
binning = int(6/0.0328) #Scott's rule for the binning
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.figure(1)  
plt.hist(e1_Ns[~np.isnan(e1_Ns)], range=[0,5], bins=binning, density=True, facecolor='b')  
plt.title("Short-term error (Ns)")
plt.text(2, 1, 'mean:' '%4f' %np.nanmean(e1_Ns))
plt.text(2, 0.6, 'std:' '%4f' %np.nanstd(e1_Ns))
plt.axis([0, 5, 0, 3.5])
plt.grid(True)
plt.show()

binning = int(6/0.0328)
plt.figure(2)  
plt.hist(e1_Ng[~np.isnan(e1_Ng)], range=[0,5], bins=binning, density=True, facecolor='b')  
plt.title("Short-term error (Ng)")
plt.text(2, 1, 'mean:' '%4f' %np.nanmean(e1_Ng))
plt.text(2, 0.6, 'std:' '%4f' %np.nanstd(e1_Ng))
plt.axis([0, 5, 0, 3.5])
plt.grid(True)
plt.show()

binning = int(6/0.0433)
plt.figure(3)  
plt.hist(e1_Nc[~np.isnan(e1_Nc)], range=[0,5], bins=binning, density=True, facecolor='b')  
plt.title("Short-term error (Nc)")
plt.text(2, 1, 'mean:' '%4f' %np.nanmean(e1_Nc))
plt.text(2, 0.6, 'std:' '%4f' %np.nanstd(e1_Nc))
plt.axis([0, 5, 0, 3.5])
plt.grid(True)
plt.show()

#====================================================================
#stability criterion combining short and long-term
#====================================================================


### Long-term error without levels
mu2_81 = err.long_term_error(Ns, period_rescaling=8, wdw=81, level=True, wdw_level=4000)
mu2_1 = err.long_term_error(Ns, period_rescaling=8, wdw=365, level=True, wdw_level=4000)
mu2_2 = err.long_term_error(Ns, period_rescaling=8, wdw=912, level=True, wdw_level=4000)
    
plt.rcParams['figure.figsize'] = (10.0, 6.0)
start = np.where(time == 1960)[0][0]
stop = np.where(time == 2010)[0][0]
stat = 19
fig = plt.figure()
plt.plot(time[start:stop], mu2_81[start:stop, stat], ':', c='tab:green', label='$\hat \mu_2$ (81)')
plt.plot(time[start:stop], mu2_1[start:stop, stat], '--', c='tab:red', label='$\hat \mu_2$ (1)')
plt.plot(time[start:stop], mu2_2[start:stop, stat], lw=3, c='tab:blue', label='$\hat \mu_2$ (2)')
plt.plot([time[start], time[stop]], [0, 0], 'k-', lw=2)
plt.legend(loc='upper right')
#f4.set_ylim([-10,20]); f4.set_xlim([time[start-20], time[stop+20]])
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 10)
plt.xticks(x_ticks)
plt.title("Long-term error for Ns in %s" %station_names[stat])
plt.ylabel('$\hat \mu_2$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
#fig.savefig('mu2_Ns_SM.pdf')
plt.show()

##########################"

mu2_81_g = err.long_term_error(Ng, period_rescaling=14, wdw=81, level=True, wdw_level=4000)
mu2_1_g = err.long_term_error(Ng, period_rescaling=14, wdw=365, level=True, wdw_level=4000)
mu2_2_g = err.long_term_error(Ng, period_rescaling=14, wdw=912, level=True, wdw_level=4000)

plt.rcParams['figure.figsize'] = (10.0, 6.0)
start = np.where(time == 1960)[0][0]
stop = np.where(time == 2010)[0][0]
stat = 19
fig = plt.figure()
plt.plot(time[start:stop], mu2_81_g[start:stop, stat], ':', c='tab:green', label='$\hat \mu_2$ (81)')
plt.plot(time[start:stop], mu2_1_g[start:stop, stat], '--', c='tab:red', label='$\hat \mu_2$ (1)')
plt.plot(time[start:stop], mu2_2_g[start:stop, stat], lw=3, c='tab:blue', label='$\hat \mu_2$ (2)')
plt.plot([time[start], time[stop]], [0, 0], 'k-', lw=2)
plt.legend(loc='lower left')
#f4.set_ylim([-10,20]); f4.set_xlim([time[start-20], time[stop+20]])
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 10)
plt.xticks(x_ticks)
plt.title("Long-term error for Ng in %s" %station_names[stat])
plt.ylabel('$\hat \mu_2$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
#fig.savefig('mu2_Ng_SM.pdf') 
plt.show()



mse_add = err.mse_criterion(e1_Ns, station_names, ref=1)[0] + \
                    err.mse_criterion(mu2_1, station_names, ref=0)[0]
ind_order = np.argsort(mse_add)
names_add = [station_names[i] for i in ind_order]

#should be the same if the errors were perfectly independent
mse_comb, names_comb = err.mse_criterion(e1_Ns+mu2_1, station_names, ref=1)

#====================================================================
#error bars
#====================================================================


add, ref = err.error_add(Ns, period_rescaling=8)

start = np.where(time == 2005)[0][0]
stop = np.where(np.round(time,1) == 2005.5)[0][0]
stat = 20

plt.stem(time[start:stop], ref[start:stop]+add[start:stop, stat], label='ref+errors', markerfmt='C0.', basefmt='C0-')
plt.plot(time[start:stop], ref[start:stop], c='tab:purple', label='ref', lw=3)
plt.legend(loc='upper right')
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start],1), np.round(time[stop],1), 0.1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 5)
plt.xticks(x_ticks)
plt.title("Additive errors in %s" %station_names[stat])
plt.ylabel('$Y_i(t)$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
plt.show()


plt.stem(time[start:stop], Ns[start:stop, stat], label='real values', markerfmt='C0.', basefmt='C0-')
plt.plot(time[start:stop], ref[start:stop], c='tab:purple', label='ref', lw=3)
plt.legend(loc='upper right')
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start],1), np.round(time[stop],1), 0.1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 5)
plt.xticks(x_ticks)
plt.title("Additive errors in %s" %station_names[stat])
plt.ylabel('$Y_i(t)$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
plt.show()

plt.stem(time[start:stop], add[start:stop, stat], label='errors', markerfmt='C0.', basefmt='C0-')
plt.plot(time[start:stop], ref[start:stop], c='tab:purple', label='ref', lw=3)
plt.legend(loc='upper right')
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start],1), np.round(time[stop],1), 0.1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 5)
plt.xticks(x_ticks)
plt.title("Additive errors in %s" %station_names[stat])
plt.ylabel('$Y_i(t)$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
plt.show()

#####################################

bars_m, bars_p, ref = err.error_bars(Ns, period_rescaling=8)

stat = 20
start = np.where(time == 2000)[0][0]
stop = np.where(np.round(time,1) == 2000.3)[0][0]

y = ref[start:stop]
bars = np.array((bars_m[start:stop,stat], bars_p[start:stop,stat]))
plt.vlines(time[start:stop], y + bars[0,:], y + bars[1,:], lw=0.8)
plt.scatter(time[start:stop], y + bars[0,:], marker='_', c='orange')
plt.scatter(time[start:stop], y + bars[1,:], marker='_', c='orange')
plt.plot(time[start:stop], y, c='tab:purple', label='ref', lw=3)
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start],1), np.round(time[stop],1), 0.1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 5)
plt.xticks(x_ticks)
plt.title("Error bars in %s" %station_names[stat])
plt.ylabel('$Y_i(t)$')
plt.xlabel('year')
plt.tick_params(axis='x', which='major')
plt.legend(loc='lower right')
plt.show()


start = np.where(np.round(time,1) == 2000.2)[0][0]
stop = np.where(np.round(time,1) == 2000.5)[0][0]
y = Ns_rescaled[start:stop, stat]

bars = np.array((bars_m[start:stop,stat], bars_p[start:stop,stat]))
plt.scatter(time[start:stop], y, c='orange', marker='+', label='Ns', lw=2)
plt.scatter(time[start:stop], y + bars[0,:], marker='_', c='tab:purple', lw=2)
plt.scatter(time[start:stop], y + bars[1,:], marker='_', c='tab:purple', lw=2)
plt.vlines(time[start:stop], y + bars[0,:], y + bars[1,:], lw=0.5)
plt.title("Error bars in %s" %station_names[stat])
plt.ylabel('$Y_i(t)$')
plt.xlabel('year')
plt.legend(loc='lower right')
if stop-start < 4000:
    x_ticks = np.arange(np.round(time[start],1), np.round(time[stop],1), 0.1)
else :
    x_ticks = np.arange(np.round(time[start]), np.round(time[stop])+1, 5)
plt.xticks(x_ticks)
plt.show()

