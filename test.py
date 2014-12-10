from scipy.interpolate import interpn

__author__ = 'Agnieszka'

import numpy as np
def _sample_2d_data():
        x = np.arange(1, 6)
        x = np.array([.5, 2., 3., 4., 5.5])
        y = np.arange(1, 6)
        y = np.array([.5, 2., 3., 4., 5.5])
        z = np.array([[1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 3, 2, 1],
                      [1, 2, 2, 2, 1], [1, 2, 1, 2, 1]])
        return x, y, z

x, y, z = _sample_2d_data()



xi = np.array([[1, 2.3, 6.3, 0.5],
                       [1, 3.3, 1.2, -4.0]]).T
actual = interpn((x, y), z, xi, method="splinef2d",
                         bounds_error=False, fill_value=999.99)