def get_data(day):
    """
    Load day data ('day1') and returns ex and data file
    
    """
    import os
    loc_path = os.getcwd()

    base_path_e = 'E:\GitHub\\aoc2022\\data'
    base_path_g = 'G:\Meu Drive\GitHUB\\aoc2022\\data'
    ex_name = '\\' + day + '_ex.txt'
    data_name = '\\' + day + '_data.txt'

    if loc_path.upper()[0] == 'E':
        file_ex = open(base_path_e + ex_name, 'r')
        file_data = open(base_path_e + data_name, 'r')
    else:
        file_ex = open(base_path_g + ex_name, 'r')
        file_data = open(base_path_g + data_name, 'r')

    return file_ex, file_data