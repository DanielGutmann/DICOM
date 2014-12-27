from matplotlib.pyplot import show, colorbar, imshow, figure
from scipy.ndimage import gaussian_filter
from Normalization import normalize

__author__ = 'Agnieszka'

import numpy as np
from scipy import interpolate


class Histogram2D(object):
    def __init__(self, No_bin_x, No_bin_y):
        self.No_bin_x = No_bin_x
        self.No_bin_y = No_bin_y
        self.H = 0

        self.angle = np.pi/4.0

    def apply(self, elevation, azimuth, weights):
        self.peaks = []

        H, e, z = np.histogram2d(elevation.flatten(), azimuth.flatten(), bins=[self.No_bin_x, self.No_bin_y],
                                 normed=False, weights=weights.flatten())
        H = normalize(H, [np.min(H), np.max(H)], [-1, 1])
        H = gaussian_filter(H, 0.1, truncate=3.0)
        self.H = normalize(H, [np.min(H), np.max(H)], [0, 1])
        peaks = self.H > 0.8
        control_sum = np.sum(peaks)
        index_peaks = np.unravel_index(self.H.argmax(), self.H.shape)
        temp = np.copy(self.H)
        temp[index_peaks] = -1000

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




    def get_Histogram2D_max(self):

        return np.array(self.peaks) * self.angle


    def get_Histogram2D(self):
        return self.H

