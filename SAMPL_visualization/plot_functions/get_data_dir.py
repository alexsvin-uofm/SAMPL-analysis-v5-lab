from pathlib import Path

"""
This script finds the data on your computer and returns the path to it. 
It also returns the frame rate of the data, which you have to ensure is correct.
"""
def get_figure_dir(pick_data):
    figures_base_path = Path.cwd() / 'figures' 
    # Construct the final path string
    save_figures_to = str(figures_base_path / pick_data)
    return save_figures_to

def get_data_dir(pick_data, which_storage='LabDataPro'):
    data_dic = {
        'blind': [r'C:\Users\alexa\OneDrive\Desktop\Data\Yunlu Z\SAMPL_data\blind_2025\toana', 166],
        
    }

    if pick_data == 'tmp':
        root = input("directory: ")
        fr = int(input("frame rate: "))
    else: 
        root = data_dic[pick_data][0]
        fr = data_dic[pick_data][1]
    return root, fr