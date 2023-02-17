import numpy as np
import pandas as pd

def load_data(path, delimiter = ';'):

    """
    Loads a CSV file from the given path and returns a pandas DataFrame.

    Parameters:
    -----------
    path : str
        The path of the CSV file to load.
    delimiter : str, optional (default ';')
        The delimiter used in the CSV file to separate values.

    Returns:
    --------
    pandas.DataFrame
        The DataFrame containing the data loaded from the CSV file.
    """

    return pd.read_csv(path, delimiter = delimiter)

def count_well(data):

    """
    Counts the number of unique well IDs in the given pandas DataFrame.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the well IDs to count.

    Returns:
    --------
    int
        The number of unique well IDs in the DataFrame.
    """

    return data.WELL.value_counts().shape[0]

def get_well_names(data):
    """
    Returns a list of unique well names in the given pandas DataFrame.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the well names to return.

    Returns:
    --------
    list
        A list of unique well names in the DataFrame.
    """

    return list(data.WELL.value_counts().index)

def get_overlapping_well(training_data, testing_data):
    """
    Finds the number and names of wells that overlap between two pandas DataFrames.

    Parameters:
    -----------
    training_data : pandas.DataFrame
        The DataFrame containing the training well data.
    testing_data : pandas.DataFrame
        The DataFrame containing the testing well data.

    Returns:
    --------
    tuple
        A tuple containing two values:
        - The number of testing wells that overlap with training wells.
        - A list of the names of the testing wells that overlap with training wells.
          If no testing wells overlap with training wells, this value is None.
    """

    count_overlapping_well = 0
    overlapped_well = []
    for well in get_well_names(testing_data):
        if well in get_well_names(training_data) == True:
            count_overlapping_well+=1
            overlapped_well.append(well)
        if count_overlapping_well !=0:
            print("Total numbers of testing wells overlapping in training wells: {} and their names are {}".format(count_overlapping_well, overlapped_well))
            return (count_overlapping_well, overlapped_well)
        else:
            print("Total numbers of testing wells overlapping in training wells: {}".format(count_overlapping_well))
            return (count_overlapping_well, None)

def get_random_well(data, seed = None):
    """
    Returns a random well from the given pandas DataFrame.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the wells to choose from.
    seed : int or None, optional (default None)
        The random seed to use for generating the well index. If None, the random
        number generator is not seeded.

    Returns:
    --------
    pandas.DataFrame
        A DataFrame containing the data for a random well chosen from the input DataFrame.
    """

    if seed:
        np.random.seed(seed)
    rand_well_index = np.random.randint(0, count_well(data))
    rand_well_name = get_well_names(data)[rand_well_index]
    print('Displaying information for Well {}'.format(rand_well_name))
    rand_well_data = data[data['WELL'] == rand_well_name]

    return rand_well_data

def percet_missing_data(dataframe):
    """
    Calculates the percentage of missing values in each column of the given pandas DataFrame.

    Parameters:
    -----------
    dataframe : pandas.DataFrame
        The DataFrame to calculate missing values for.

    Returns:
    --------
    pandas.Series
        A Series object with the percentage of missing values for each column in the input DataFrame.
    """
    
    return dataframe.isna().sum()/dataframe.shape[0]*100

def group_identification(data):
    """
    Prints and returns the names of the unique groups in the given pandas DataFrame.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame to identify unique groups in.

    Returns:
    --------
    pandas.Index
        A pandas Index object containing the names of the unique groups in the input DataFrame.
    """
    value_counts = data.GROUP.value_counts()
    print('Displaying all the GROPUs available in the dataset\nTotal {} GROUPS found in the dataset'.format(value_counts.count()))
    print(value_counts)
    return value_counts.index

def remove_column_with_half_of_nan_value(data):
    """
    Removes columns from the given pandas DataFrame that have more than 50% missing values.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame to remove columns from.

    Returns:
    --------
    None
    """
    
    print("Removing columns which have 50% of missing data i.e., 'SGR', 'ROP', 'DTS', 'DCAL', 'MUDWEIGHT', 'RMIC', 'ROPA', 'RXO', 'BS', 'DRHO'")
    data.drop(['SGR', 'ROP', 'DTS', 'DCAL', 'MUDWEIGHT', 'RMIC', 'ROPA', 'RXO', 'BS', 'DRHO'], axis = 1, inplace = True)