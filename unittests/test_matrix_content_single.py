#!/usr/bin/env python
# coding: utf8

import sys, os
import unittest
import numpy as np

sys.path.insert(0, os.path.dirname(__file__) + "../")

from kernel.td_kernel_dmvw import TDKernelDMVW

# Set parameters
min_x = 0
min_y = 0
max_x = 70
max_y = 50
cell_size = 1
kernel_size = 10 * cell_size
wind_scale = 0.05
time_scale = 0.001
evaluation_radius = 10*kernel_size

# Create dummy measurement vectors
positions_x = [20]
positions_y = [40]
concentrations = [10]
wind_directions = [0]
wind_speeds = [0]
timestamps = [0]

number_of_x_cells = (max_x - min_x) / cell_size + 1
number_of_y_cells = (max_y - min_y) / cell_size + 1

class TestMatrixContentSingle(unittest.TestCase):

    def setUp(self):
        self.kernel = TDKernelDMVW(min_x, min_y, max_x, max_y, cell_size, kernel_size, wind_scale, time_scale, low_confidence_calculation_zero=True, evaluation_radius=evaluation_radius)

    def calculate(self):
        self.kernel.set_measurements(positions_x, positions_y, concentrations, timestamps, wind_speeds, wind_directions)
        self.kernel.calculate_maps()

    def testMeanValues(self):
        self.calculate()

	# Implies, that x is the first index (0)
        self.assertEqual(71, self.kernel.mean_map.shape[0])
        self.assertEqual(51, self.kernel.mean_map.shape[1])

        self.assertTrue(self.kernel.importance_weight_map[20][40] > self.kernel.importance_weight_map[40][20])
        self.assertTrue(self.kernel.mean_map[20][40] > self.kernel.mean_map[40][20])

if __name__ == '__main__':
    unittest.main()
