import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def plot3Dlocation(rand_well):
    """
    Plots a 3D visualization of the well path for a given well.

    Parameters:
    -----------
    rand_well : pandas.DataFrame
        A DataFrame containing the data for a single well, including columns for X_LOC, Y_LOC, and Z_LOC.

    Returns:
    --------
    None
        The function displays the 3D visualization in a new window using matplotlib and does not return anything.
    """

    x_loc = rand_well.X_LOC
    y_loc = rand_well.Y_LOC
    z_loc = np.abs(rand_well.Z_LOC)

    fig = plt.figure(figsize=(12, 12))
    ax = plt.axes(projection='3d')
    ax.plot3D(x_loc, y_loc, np.abs(z_loc))

    ax.plot3D(x_loc.values[0], y_loc.values[0], z_loc.values[0], marker='s', color='black', ms=8)
    ax.plot3D(x_loc.values[-1], y_loc.values[-1], z_loc.values[-1], marker='*', color='red', ms=8)
    ax.set_xlabel('X Location')
    ax.set_ylabel('Y Location')
    ax.set_zlabel('TVD')
    ax.invert_zaxis()
    plt.show()

def plot2Dlocation(rand_well):
    """
    Plots the X and Y locations, as well as the X and TVDss and Y and TVDss plots
    of a random well using the provided data in a pandas DataFrame.

    Parameters:
    -----------
    rand_well : pandas.DataFrame
        The well data to plot. Must contain columns with X_LOC, Y_LOC, and Z_LOC.

    Returns:
    --------
    None
        The function displays the 2D visualization in a new window using matplotlib and does not return anything.
    """

    x_loc = rand_well.X_LOC
    y_loc = rand_well.Y_LOC
    z_loc = np.abs(rand_well.Z_LOC)

    _, ax = plt.subplots(1, 3, figsize = (20, 5))

    ax[0].plot(x_loc, y_loc)
    ax[0].set_title('X Location vs Y Location')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    ax[0].set_xlabel('X')
    ax[0].set_ylabel('Y')

    ax[1].plot(x_loc, z_loc)
    ax[1].set_title('X Location vs TVDss')
    ax[1].set_xticks([])
    ax[1].set_xlabel('X')
    ax[1].set_ylabel('TVDss')
    ax[1].plot(x_loc.values[0], z_loc.values[0], marker='s', color='black', ms=8)
    ax[1].plot(x_loc.values[-1], z_loc.values[-1], marker='*', color='red', ms=8)
    ax[2].invert_yaxis()

    ax[2].plot(y_loc, z_loc)
    ax[2].set_title('Y Location vs TVDss')
    ax[2].set_xticks([])
    ax[2].set_xlabel('Y')
    ax[2].set_ylabel('TVDss')
    ax[2].plot(y_loc.values[0], z_loc.values[0], marker='s', color='black', ms=8)
    ax[2].plot(y_loc.values[-1], z_loc.values[-1], marker='*', color='red', ms=8)
    ax[2].invert_yaxis()
    plt.show()

def xaxis(ax, xmin, xmax, spines_pos, color, log_name, name_size, y):
    """
    Set the properties of the x-axis of a matplotlib plot.
    Parameters:
    -----------
    ax : matplotlib.axes.Axes object
        The axes object on which to set the x-axis properties.
    xmin : float
        The minimum value to be shown on the x-axis.
    xmax : float
        The maximum value to be shown on the x-axis.
    spines_pos : float
        The position of the x-axis spines (in points) relative to the plot.
    color : str
        The color of the x-axis and its labels.
    log_name : str
        The name of the x-axis label.
    name_size : int
        The size of the x-axis label.
    y : float
        The y-coordinate of the x-axis label.

    Returns:
    --------
    None
    """
    ax.set_xticks((xmin, xmax))
    ax.spines['top'].set_position(('outward', spines_pos))
    ax.spines['top'].set_color(color)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_label_coords(0.5, y)
    ax.set_xlabel(log_name, color = color, size = name_size)
    ax.tick_params(axis = 'x', colors = color, size = 0, labelsize = 10)

def log_plot(logs):
    """
    Plot well log data using a five-panel plot with shared y-axis.

    Parameters:
    -----------
    logs : pandas.DataFrame
        DataFrame containing well log data. It should have columns for depth
        (DEPTH_MD) and at least the following logs: CALI, GR, SP, RSHA, RMED,
        RDEP, RHOB, NPHI, and DTC. Other columns will be ignored.

    Returns:
    --------
    None
    """
    
    _, ax = plt.subplots(1,5, figsize = (10, 15), sharey = True)
    ax[0].invert_yaxis()
    ax[0].grid()

    ax_gr_wrap = ax[0].twiny()
    ax_sp_wrap = ax[0].twiny()

    ax_rm_wrap = ax[1].twiny()
    ax_rd_wrap = ax[1].twiny()

    ax_nphi_wrap = ax[2].twiny()

    ax[0].plot(logs.CALI, list(range(logs.DEPTH_MD.shape[0])), 'b')
    ax_gr_wrap.plot(logs.GR, list(range(logs.DEPTH_MD.shape[0])), 'r')
    ax_sp_wrap.plot(logs.SP, list(range(logs.DEPTH_MD.shape[0])), 'g' )

    ax[1].plot(logs.RSHA, list(range(logs.DEPTH_MD.shape[0])), 'b')
    ax_rm_wrap.plot(logs.RMED, list(range(logs.DEPTH_MD.shape[0])), 'r')
    ax_rd_wrap.plot(logs.RDEP, list(range(logs.DEPTH_MD.shape[0])), 'g')

    ax[2].plot(logs.RHOB, list(range(logs.DEPTH_MD.shape[0])), 'b')
    ax_nphi_wrap.plot(logs.NPHI, list(range(logs.DEPTH_MD.shape[0])), 'r')

    ax[3].plot(logs.DTC, list(range(logs.DEPTH_MD.shape[0])), 'b')

    ax[0].set_xlim(6, 24)
    ax_gr_wrap.set_xlim(0, 150)
    ax_sp_wrap.set_xlim(-150, 150)

    ax[1].set_xlim(0.2, 200)
    ax_rm_wrap.set_xlim(0.2, 200)
    ax_rd_wrap.set_xlim(0.2, 200)

    ax[1].set_xscale('log')
    #ax_rm_wrap.set_xscale('log')
    #ax_rd_wrap.set_xscale('log')

    ax[2].set_xlim(0.95, 2.95)
    ax_nphi_wrap.set_xlim(-0.15, 1.05)
    ax_nphi_wrap.invert_xaxis()

    ax[3].set_xlim(40, 240)
    ax[3].invert_xaxis()

    logs_group_temp = logs.GROUP.fillna('N/A')
    encoder_temp = LabelEncoder()
    encoder_temp.fit(logs_group_temp)
    logs_group_temp_encoded = pd.Series(encoder_temp.transform(logs_group_temp))
    cl = np.repeat(np.expand_dims(logs_group_temp_encoded.values,1), 200, 1)
    ax[4].imshow(cl, interpolation='none', aspect='auto')


    ax[4].set_xticklabels([])

    xaxis(ax[0], 6, 24, 0, 'b', 'CALI', 10, 1.003)
    xaxis(ax_gr_wrap, 0, 150, 25, 'r', 'GR', 10, 1.029)
    xaxis(ax_sp_wrap, -150, 150, 50, 'g', 'SP', 10, 1.051)

    xaxis(ax[1], 0, 200, 0, 'b', 'Rs', 10, 1.003)
    xaxis(ax_rm_wrap, 0.2, 200, 25, 'r', 'Rm', 10, 1.029)
    xaxis(ax_rd_wrap, 0.2, 200, 50, 'g', 'Rd', 10, 1.051)

    xaxis(ax[2], 0.95, 2.95, 0, 'b', 'RHOB', 10, 1.003)
    xaxis(ax_nphi_wrap, -0.15, 1.05, 25, 'r', 'NPHI', 10, 1.029)

    xaxis(ax[3], 40, 240, 0, 'b', 'Sonic', 10, 1.003)

    ax[4].set_title('Group')

    plt.show()