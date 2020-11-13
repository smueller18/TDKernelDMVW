import matplotlib.pyplot as plt

from td_kernel_dmvw.td_kernel_dmvw import TDKernelDMVW

__author__ = u'Stephan Müller'
__copyright__ = u'2017, Stephan Müller'
__license__ = u'MIT'

# Set parameters
min_x = 0
min_y = 0
max_x = 20
max_y = 20
cell_size = 0.1
kernel_size = 10 * cell_size
wind_scale = 0.05
time_scale = 0.001
evaluation_radius = 10 * kernel_size

# Create dummy measurement vectors
positions_x = [4, 6.5, 15]
positions_y = [2, 6.5, 15]
concentrations = [2, 2, 2]
wind_directions = [0, 60, 0]
wind_speeds = [0, 1, 0]
timestamps = [0, 60, 60]

# call Kernel
kernel = TDKernelDMVW(min_x, min_y, max_x, max_y, cell_size, kernel_size, wind_scale, time_scale,
                      low_confidence_calculation_zero=True, evaluation_radius=evaluation_radius)
kernel.set_measurements(positions_x, positions_y, concentrations, timestamps, wind_speeds, wind_directions)
kernel.calculate_maps()

# Show result as map
plt.figure()
plt.title("mean map")
plt.contourf(kernel.cell_grid_x, kernel.cell_grid_y, kernel.mean_map)
plt.colorbar()

plt.figure()
plt.title("variance map")
plt.contourf(kernel.cell_grid_x, kernel.cell_grid_y, kernel.variance_map)
plt.colorbar()

plt.figure()
plt.title("confidence map")
plt.contourf(kernel.cell_grid_x, kernel.cell_grid_y, kernel.confidence_map)
plt.colorbar()

plt.show()
