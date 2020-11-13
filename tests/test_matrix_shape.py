from td_kernel_dmvw.td_kernel_dmvw import TDKernelDMVW

# Set parameters
min_x = 0
min_y = 0
max_x = 10
max_y = 5
cell_size = 1
kernel_size = 10 * cell_size
wind_scale = 0.05
time_scale = 0.001
evaluation_radius = 10 * kernel_size

# Create dummy measurement vectors
positions_x = [2, 5, 5]
positions_y = [2, 3, 2]
concentrations = [2, 2, 2]
wind_directions = [0, 0, 0]
wind_speeds = [0, 0, 0]
timestamps = [0, 0, 0]

number_of_x_cells = (max_x - min_x) / cell_size + 1
number_of_y_cells = (max_y - min_y) / cell_size + 1


class TestMatrixShape:

    @classmethod
    def setup_class(cls):
        cls.kernel = TDKernelDMVW(min_x, min_y, max_x, max_y, cell_size, kernel_size, wind_scale, time_scale,
                                  low_confidence_calculation_zero=True, evaluation_radius=evaluation_radius)
        cls.kernel.set_measurements(positions_x, positions_y, concentrations, timestamps, wind_speeds, wind_directions)
        cls.kernel.calculate_maps()

    def test_bbox(self):
        assert number_of_x_cells == self.kernel.number_of_x_cells
        assert number_of_y_cells == self.kernel.number_of_y_cells

        assert min_x == self.kernel.min_x
        assert min_y == self.kernel.min_y

        # BBox is increased to handle python floats properly
        assert min_x + round(number_of_x_cells * cell_size, 10) == self.kernel.max_x
        assert min_y + round(number_of_y_cells * cell_size, 10) == self.kernel.max_y

    def test_cell_grids(self):
        assert number_of_x_cells == self.kernel.cell_grid_x.shape[0]
        assert number_of_x_cells == self.kernel.cell_grid_y.shape[0]
        assert number_of_y_cells == self.kernel.cell_grid_x.shape[1]
        assert number_of_y_cells == self.kernel.cell_grid_y.shape[1]

    def test_mean_shape(self):
        assert number_of_x_cells == self.kernel.mean_map.shape[0]
        assert number_of_y_cells == self.kernel.mean_map.shape[1]

    def test_variance_shape(self):
        assert number_of_x_cells == self.kernel.variance_map.shape[0]
        assert number_of_y_cells == self.kernel.variance_map.shape[1]

    def test_confidence_shape(self):
        assert number_of_x_cells == self.kernel.confidence_map.shape[0]
        assert number_of_y_cells == self.kernel.confidence_map.shape[1]

    def test_importance_shape(self):
        assert number_of_x_cells == self.kernel.importance_weight_map.shape[0]
        assert number_of_y_cells == self.kernel.importance_weight_map.shape[1]
