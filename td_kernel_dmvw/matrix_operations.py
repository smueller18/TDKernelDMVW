import numpy as np

__author__ = u'Stephan Müller'
__copyright__ = u'2017, Stephan Müller'
__license__ = u'MIT'


def get_position_of_minimum(matrix):
    return np.unravel_index(np.nanargmin(matrix), matrix.shape)


def get_position_of_maximum(matrix):
    return np.unravel_index(np.nanargmax(matrix), matrix.shape)


def get_distance_matrix(cell_grid_x, cell_grid_y, x, y):
    return np.sqrt((x - cell_grid_x) ** 2 + (y - cell_grid_y) ** 2)


def get_distance_matrix_squared(cell_grid_x, cell_grid_y, x, y):
    return (x - cell_grid_x) ** 2 + (y - cell_grid_y) ** 2
