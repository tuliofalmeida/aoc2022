def get_data(day):
    """
    Load day data ('day1') and returns ex and data file
    
    """
    import os
    loc_path = os.getcwd().capitalize()

    file_ex = open(loc_path + '\\data\\' + day + '_ex.txt','r')
    file_data = open(loc_path + '\\data\\' + day + '_data.txt','r')

    return file_ex, file_data