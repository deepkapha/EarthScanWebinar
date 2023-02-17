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
    Identifies the unique groups in the given pandas DataFrame.

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
    return value_counts

def remove_column_with_half_of_nan_value(data):
    """
    Remove columns from the input data that have more than 50% missing values.

    Parameters
    ----------
    data: pandas DataFrame
        The input data.

    Returns
    -------
    pandas DataFrame
        The modified input data with selected columns removed.
    """

    print("Removing columns which have 50% of missing data i.e., 'SGR', 'ROP', 'DTS', 'DCAL', 'MUDWEIGHT', 'RMIC', 'ROPA', 'RXO', 'BS', 'DRHO'")
    data = data.drop(['SGR', 'ROP', 'DTS', 'DCAL', 'MUDWEIGHT', 'RMIC', 'ROPA', 'RXO', 'BS', 'DRHO'], axis = 1)
    return data

def get_nonoverlapping_groups(train_group, test_group):
    """
    Returns the names of the groups that appear in the testing data but not in the training data.

    Parameters:
    -----------
    train_group : pandas.Index
        A pandas Index object containing the names of the unique groups in the training data.

    test_group : pandas.Index
        A pandas Index object containing the names of the unique groups in the testing data.

    Returns:
    --------
    tuple
        A tuple containing two elements:
            - the number of groups in the testing data that do not appear in the training data
            - a list of the names of those groups
    """

    count_nonoverlapping_groups = 0
    nonoverlapped_groups = []
    for group in test_group:
        if (group in train_group) == False:
            count_nonoverlapping_groups+=1
            nonoverlapped_groups.append(group)
    if count_nonoverlapping_groups !=0:
        print("Total numbers of GROUPS in testing wells that is not overlapping in training wells: {} and their names are {}".format(count_nonoverlapping_groups, nonoverlapped_groups))
        return (count_nonoverlapping_groups, nonoverlapped_groups)
    else:
        print("Total numbers of GROUPS in testing wells that is not overlapping in training wells: {}".format(count_nonoverlapping_groups))
        return (count_nonoverlapping_groups, None)

def missing_group_info(data):
    """
    Prints the number of data points with missing group information in the given DataFrame.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the data to be checked for missing group information.

    Returns:
    --------
    None
    """
    
    print('Total data points with missing Group information: {}'.format(data.GROUP.isna().sum()))

def remove_formation_column(data):
    """
    Remove the 'FORMATION' column from the input dataset.

    Parameters:
    -----------
    data : pandas.DataFrame
        Input dataset from which the 'FORMATION' column needs to be removed.

    Returns:
    --------
    pandas.DataFrame
        A new DataFrame with the 'FORMATION' column removed.
    """

    print('Removing FORMATION column from the dataset')
    data = data.drop(['FORMATION'], axis = 1)
    return data

def get_undeviated_well_info(data):
    """
    Returns a list of names of undeviated wells in the given DataFrame.

    An undeviated well is defined as a well where all data points have the same X and Y coordinates.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame from which to extract undeviated well names.

    Returns:
    --------
    well_names : list of str
        A list of names of undeviated wells in the input DataFrame.
    """
    
    well_names = []
    for well_name in preprocessing.get_well_names(data):
        well_data = data[data.WELL == well_name]
        if (well_data.X_LOC.value_counts().shape[0] == 1) and (well_data.Y_LOC.value_counts().shape[0] == 1):
            well_names.append(well_name)
            
    print('Total Number of undeviated wells present in the dataset is {} and their names are:\n{}'.format(len(well_names), 
                                                                                                          well_names))
    return well_names

def get_well_with_missing_group_info(data, total_num_wells, well_names):
    """
    Returns a list of well names that have missing information on the 'GROUP' column in the input dataset.

    Parameters:
    -----------
    data : pandas.DataFrame
        The input dataset containing well information.
    total_num_wells : int
        The total number of wells in the dataset.
    well_names : list of str
        A list of well names in the dataset.

    Returns:
    --------
    list of str
        A list of well names that have missing information on the 'GROUP' column in the input dataset.
    """
    
    well_with_missing_group_info = []

    for well_names_index in range(total_num_wells):
        single_well_name = well_names[well_names_index]
        single_well_data = data[data['WELL'] == single_well_name]
        total_group_data_missing = single_well_data.GROUP.isna().sum()
        if total_group_data_missing != 0:
            print('Well "{0}" is having missing information on GROUP and total data points missing this information is {1}'.format(single_well_name, total_group_data_missing))
            well_with_missing_group_info.append(single_well_name)
    print('\nTotal {} Wells have missing group information!'.format(len(well_with_missing_group_info)))
    return well_with_missing_group_info

def fill_group_na_value(data, well_name, method = 'bfill'):
    """
    Fills the missing GROUP values for the given well in the DataFrame.

    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the well data.
    well_name : str
        The name of the well to fill missing GROUP values for.
    method : str, optional (default 'bfill')
        The method used to fill missing values. It can be one of {'backfill', 'bfill', 'ffill', 'pad', 'nearest'}.

    Returns:
    --------
    pandas.Series
        The Series containing the filled GROUP values for the given well.
    """
    
    return data[data['WELL'] == well_name].GROUP.fillna(method = method)