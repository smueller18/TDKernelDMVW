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
max_x = 10
max_y = 5
cell_size = 1
kernel_size = 10 * cell_size
wind_scale = 0.05
time_scale = 0.001
evaluation_radius = 10*kernel_size

# Create dummy measurement vectors
positions_x = [2, 5, 5]
positions_y = [2, 3, 2]
concentrations = [2, 2, 2]
wind_directions = [0, 0, 0]
wind_speeds = [0, 0, 0]
timestamps = [0, 0, 0]

number_of_x_cells = (max_x - min_x) / cell_size + 1
number_of_y_cells = (max_y - min_y) / cell_size + 1

class TestCalcLocalMaxima(unittest.TestCase):

    def setUp(self):
        self.kernel = TDKernelDMVW(min_x, min_y, max_x, max_y, cell_size, kernel_size, wind_scale, time_scale, low_confidence_calculation_zero=True, evaluation_radius=evaluation_radius)

    def calculate(self):
        self.kernel.set_measurements(positions_x, positions_y, concentrations, timestamps, wind_speeds, wind_directions)
        self.kernel.calculate_maps()

    def testBBox(self):

        self.assertEqual(number_of_x_cells, self.kernel.number_of_x_cells)
        self.assertEqual(number_of_y_cells, self.kernel.number_of_y_cells)

        self.assertEqual(min_x, self.kernel.min_x)
        self.assertEqual(min_y, self.kernel.min_y)

	# BBox is increased to handle python floats properly
        self.assertEqual(min_x + round(number_of_x_cells * cell_size, 10), self.kernel.max_x)
        self.assertEqual(min_y + round(number_of_y_cells * cell_size, 10), self.kernel.max_y)

    def testCellGrids(self):
        self.assertEqual(number_of_x_cells, self.kernel.cell_grid_x.shape[0])
        self.assertEqual(number_of_x_cells, self.kernel.cell_grid_y.shape[0])
        self.assertEqual(number_of_y_cells, self.kernel.cell_grid_x.shape[1])
        self.assertEqual(number_of_y_cells, self.kernel.cell_grid_y.shape[1])

    def testMeanShape(self):
        self.calculate()
        self.assertEqual(number_of_x_cells, self.kernel.mean_map.shape[0])
        self.assertEqual(number_of_y_cells, self.kernel.mean_map.shape[1])

    def testVarianceShape(self):
        self.calculate()
        self.assertEqual(number_of_x_cells, self.kernel.variance_map.shape[0])
        self.assertEqual(number_of_y_cells, self.kernel.variance_map.shape[1])

    def testConfidenceShape(self):
        self.calculate()
        self.assertEqual(number_of_x_cells, self.kernel.confidence_map.shape[0])
        self.assertEqual(number_of_y_cells, self.kernel.confidence_map.shape[1])

#    def test_localmax(self):
#        kernel.set_measurements(positions_x, positions_y, concentrations, timestamps, wind_speeds, wind_directions)



if __name__ == '__main__':
    unittest.main()
