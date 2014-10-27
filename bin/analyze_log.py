#!/usr/bin/env python

import cPickle
import sys
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import math

def smooth(x,window_len=11,window='hanning'):
  if type(x) == list:
    x = np.array(x)
  if x.ndim != 1:
    raise ValueError, "smooth only accepts 1 dimension arrays."
  if x.size < window_len:
    raise ValueError, "Input vector needs to be bigger than window size."
  if window_len<3:
    return x
  if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
    raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
  s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
  if window == 'flat': #moving average
    w=np.ones(window_len,'d')
  else:  
    w=eval('np.'+window+'(window_len)')
    y=np.convolve(w/w.sum(),s,mode='same')
    return y[window_len:-window_len+1]

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "USAGE:", sys.argv[0], "pickle_log_file"
    sys.exit()
  data = cPickle.load(open(sys.argv[1], "rb"))
  
  gs = gridspec.GridSpec(2, 3)
 
  plt.subplot(gs[:, 0])
  plt.hexbin([x for t, x, y, r in data["xyr"]], [y for t, x, y, r in data["xyr"]], [r for t, x, y, r in data["xyr"]], gridsize=20, cmap=plt.get_cmap("gnuplot2"), vmin=-80, vmax=-20, extent=(-10, 0, -15, 20))
  plt.plot([x for t, x, y, r in data["xyr"]], [y for t, x, y, r in data["xyr"]], "g-")
  plt.gca().set_xlim((-10, 0))
  plt.gca().set_xlabel("x [m]")
  plt.gca().set_ylim((-15, 20))
  plt.gca().set_ylabel("y [m]")
  cbar = plt.colorbar()
  cbar.set_label("mean rssi [dB]")
  plt.subplot(gs[0, 1:])
  plt.plot([rssi[0]-data["xyr"][0][0] for rssi in data["xyr"]], [rssi[3] for rssi in data["xyr"]], "b.")
  plt.plot([rssi[0]-data["xyr"][0][0] for rssi in data["xyr"]], smooth([rssi[3] for rssi in data["xyr"]], 100), "r-")
  plt.gca().set_xlabel("time [s]")
  plt.gca().set_ylabel("rssi [dB]")
  plt.gca().set_ylim((-80, -20))
  plt.subplot(gs[1, 1:])
  trajectory = [data["xyr"][i][1:3] for i in range(len(data["xyr"]))]
  lengths = [math.hypot(trajectory[i][0] - trajectory[i-1][0], trajectory[i][1]-trajectory[i][1]) for i in range(1, len(trajectory))]
  dist = [0.0]
  for length in lengths:
    dist.append(dist[-1]+length)
  plt.plot(dist, [rssi[3] for rssi in data["xyr"]], "b.")
  plt.plot(dist, smooth([rssi[3] for rssi in data["xyr"]], 100), "r-")
  plt.gca().set_xlabel("distance travelled [m]")
  plt.gca().set_ylabel("rssi [dB]")
  plt.gca().set_ylim((-80, -20))
  plt.show()
