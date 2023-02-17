from matplotlib import pyplot as plt
import random
import csv
from utils.well_log_plots import log_plots
from PIL import Image

def log_plot_image(logs,plotname,txtname,i,patch_height):
    """
    Plots a set of well log curves for a specified depth interval in a given logs DataFrame and saves the resulting image
    to a file. It also saves a text file containing the lithology labels for the same depth interval.

    Args:
    - logs: pandas DataFrame containing well log data.
    - plotname: string specifying the name of the output image file.
    - txtname: string specifying the name of the output text file.
    - i: integer specifying the index of the top of the depth interval of interest.
    - patch_height: integer specifying the height of the depth interval of interest.

    Returns: None
    """

    _, ax = plt.subplots(1,19, figsize = (20, 10), sharey = True, gridspec_kw = {'wspace':0, 'hspace':0})
    for axis in ax:
        axis.invert_yaxis()
        axis.axis('off')

    ax[0].plot(logs.CALI[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[0].set_xlim(6, 24)

    ax[1].plot(logs.GR[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[1].set_xlim(0, 150)

    ax[2].plot(logs.SP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[2].set_xlim(-150, 150)

    ax[3].plot(logs.SGR[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[3].set_xlim(0, 150)

    ax[4].semilogx(logs.RSHA[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[4].set_xlim(2, 200)

    ax[5].semilogx(logs.RMED[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[5].set_xlim(2, 200)

    ax[6].semilogx(logs.RDEP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[6].set_xlim(2, 200)

    ax[7].semilogx(logs.RXO[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[7].set_xlim(2, 200)

    ax[8].semilogx(logs.RMIC[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[8].set_xlim(2, 200)

    ax[9].plot(logs.NPHI[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[9].set_xlim(-0.15, 1.05)
    ax[9].invert_xaxis()

    ax[10].plot(logs.RHOB[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[10].set_xlim(0.95, 2.95)
    ax[10].invert_xaxis()

    ax[11].plot(logs.PEF[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[11].set_xlim(0, 10)

    ax[12].plot(logs.ROP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[12].set_xlim(0, 50)

    ax[13].plot(logs.ROPA[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[13].set_xlim(0, 50)

    ax[14].plot(logs.DRHO[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[14].set_xlim(-0.2, 1)

    ax[15].plot(logs.DTC[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[15].set_xlim(40, 240)
    ax[15].invert_xaxis()

    ax[16].plot(logs.DTS[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[16].set_xlim(40, 240)
    ax[16].invert_xaxis()

    ax[17].plot(logs.MUDWEIGHT[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[17].set_xlim(0, 150)

    ax[18].plot(logs.BS[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[18].set_xlim(6, 24)

    plt.savefig(plotname,bbox_inches ="tight",transparent = False)

    with open(txtname, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
    # write a row to the csv file
        writer.writerow(logs.GROUP[i:i+patch_height][:-1].T)
        f.close()

def randon_list_generator():
    """
    Generate a random list of 19 unique integers between 0 and 18 (inclusive).

    This function generates a random list of 19 unique integers between 0 and 18 (inclusive)
    by using the Python's built-in random module. The function recursively calls itself until
    it generates a list with the desired number of unique integers.

    Parameters:
    -----------
    None

    Returns:
    --------
    A list of 19 unique integers between 0 and 18 (inclusive).
    """
    randomlist = []
    for i in range(0,50):
        n = random.randint(0,18)
        if n not in randomlist:
            randomlist.append(n)
    if len(randomlist) == 19: 
        return randomlist
    else:
        return randon_list_generator()

def log_plot_image_random(logs,plotname,txtname,i,patch_height,randomlist,well_train,well_train_names):
    """
    Creates a plot of log curves for a random selection of wells, and saves the plot to a file. Also saves the group
    data to a text file.

    Parameters:
    logs (pandas.DataFrame): DataFrame containing log data.
    plotname (str): Name of the output plot file.
    txtname (str): Name of the output text file.
    i (int): Starting index for the patch of data.
    patch_height (int): Number of data points in the patch.
    randomlist (list): List of indices for the randomly selected wells to plot.
    well_train (pandas.DataFrame): DataFrame containing well data.
    well_train_names (list): List of well names.

    Returns:
    None
    """
    
    _, ax = plt.subplots(1,19, figsize = (20, 10), sharey = True, gridspec_kw = {'wspace':0, 'hspace':0})
    j=0
    for i in randomlist:
        op= log_plots[i]
        op(well_train[well_train['WELL'] == well_train_names[0]],ax[j],0,700)
        j=j+1
    plt.savefig(plotname,bbox_inches ="tight",transparent = False)


    with open(txtname, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(logs.GROUP[i:i+patch_height])
        f.close()

def log_plot_image_invert(logs,plotname,txtname,i,patch_height):
    """
    Creates a plot of log curves and saves it to a file, as well as a CSV file containing log data.

    Parameters:
        logs (pandas.DataFrame): A DataFrame containing the log data.
        plotname (str): The name of the output plot file.
        txtname (str): The name of the output CSV file.
        i (int): The index of the starting depth.
        patch_height (int): The number of rows of log data to include in the plot and CSV file.

    Returns:
        None.
    """

    _, ax = plt.subplots(1,19, figsize = (20, 10), sharey = True, gridspec_kw = {'wspace':0, 'hspace':0})
    for axis in ax:
        axis.invert_yaxis()
        axis.axis('off')

    ax[0].plot(logs.CALI[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[0].set_xlim(6, 24)

    ax[1].plot(logs.GR[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[1].set_xlim(0, 150)

    ax[2].plot(logs.SP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[2].set_xlim(-150, 150)

    ax[3].plot(logs.SGR[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[3].set_xlim(0, 150)

    ax[4].semilogx(logs.RSHA[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[4].set_xlim(2, 200)

    ax[5].semilogx(logs.RMED[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[5].set_xlim(2, 200)

    ax[6].semilogx(logs.RDEP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[6].set_xlim(2, 200)

    ax[7].semilogx(logs.RXO[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[7].set_xlim(2, 200)

    ax[8].semilogx(logs.RMIC[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[8].set_xlim(2, 200)

    ax[9].plot(logs.NPHI[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[9].set_xlim(-0.15, 1.05)
    ax[9].invert_xaxis()

    ax[10].plot(logs.RHOB[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[10].set_xlim(0.95, 2.95)
    ax[10].invert_xaxis()

    ax[11].plot(logs.PEF[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[11].set_xlim(0, 10)

    ax[12].plot(logs.ROP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[12].set_xlim(0, 50)

    ax[13].plot(logs.ROPA[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[13].set_xlim(0, 50)

    ax[14].plot(logs.DRHO[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[14].set_xlim(-0.2, 1)

    ax[15].plot(logs.DTC[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[15].set_xlim(40, 240)
    ax[15].invert_xaxis()

    ax[16].plot(logs.DTS[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[16].set_xlim(40, 240)
    ax[16].invert_xaxis()

    ax[17].plot(logs.MUDWEIGHT[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[17].set_xlim(0, 150)

    ax[18].plot(logs.BS[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax[18].set_xlim(6, 24)
     
    plt.savefig(plotname,bbox_inches ="tight",transparent = False)
    im = Image.open(plotname)
    newsize = (800, 360)
    im = im.resize(newsize)
    im =im.save(plotname)

    with open(txtname, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
    # write a row to the csv file
        writer.writerow(logs.GROUP[i:i+patch_height])
        f.close()
