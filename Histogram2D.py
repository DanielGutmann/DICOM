from scipy.ndimage import gaussian_filter

__author__ = 'Agnieszka'

import numpy as np
from scipy import interpolate


class Histogram2D(object):
    def __init__(self, No_bin_x, No_bin_y):
        self.No_bin_x = No_bin_x
        self.No_bin_y = No_bin_y
        self.H = 0
        self.peaks = []
        self.angle = 45

    def apply(self, elevation, azimuth, weights):
        self.peaks = []
        self.H, e, z = np.histogram2d(elevation.flatten(), azimuth.flatten(), bins=[self.No_bin_x, self.No_bin_y],
                                      normed=False, weights=weights.flatten())
        self.H = (self.H - np.min(self.H)) / (np.max(self.H) - np.min(self.H))
        self.H = gaussian_filter(self.H, 0.1, truncate=3.0)
        peaks = self.H > 0.8
        control_sum = np.sum(peaks)
        index_peaks = np.unravel_index(self.H.argmax(), self.H.shape)
        temp = np.copy(self.H)
        temp[index_peaks] = -1000
        print peaks
        if control_sum == 1:
            self.peaks.append(index_peaks)
        elif control_sum == 2:
            self.peaks.append(index_peaks)

            index_peaks_80 = np.unravel_index(temp.argmax(), self.H.shape)
            self.peaks.append(index_peaks_80)
        elif control_sum > 2:
            self.peaks.append(index_peaks)
            index_peaks_80 = np.unravel_index(temp.argmax(), self.H.shape)
            self.peaks.append(index_peaks_80)

        print(self.peaks)


    def get_Histogram2D_max(self):
        return np.array(self.peaks) * self.angle


    def get_Histogram2D(self):
        return self.H

