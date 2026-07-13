from SAMPL_visualization.plot_functions.get_data_dir import get_data_dir
import os

root, FRAME_RATE = get_data_dir("blind")
print(root)
print(os.path.exists(root))