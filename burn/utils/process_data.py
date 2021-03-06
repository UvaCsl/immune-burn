def read_data(csvfilename):
    x, y = [], []
    with open(csvfilename + '.csv') as csvfile:
        reader = c.DictReader(csvfile)
        for row in reader:
            x.append(float(row['time']))
            y.append(float(row['concentration']))
    return x, y

def interpolate_data(csvfilename, num, plot, time, _stoptime):
    x, y = read_data(csvfilename)
    if time == 'sec':
        x_ = np.linspace(0, _stoptime / 3600., num=num, endpoint=True)
    elif time == 'min':
        x_ = np.linspace(0, _stoptime / 60., num=num, endpoint=True)
    elif time == 'hours':
        x_ = np.linspace(0, _stoptime / 1., num=num, endpoint=True)
    elif time == 'days':
        x_ = np.linspace(0, _stoptime * 24, num=num, endpoint=True)
    f = interp1d(x, y)
    if plot:
        return np.linspace(0, _stoptime, num), f(x_)
    else:
        return f(x_)
    
def group_dataframes(df, column, time, group_column='days_since_admission', agg_list=['median', 'std']):
    """ Group dataframes according to group_column.
    
    Args:
    df: Dataframe. Input Dataframe
    column: str. Immune cell column name
    time: str. Time column name
    group_column: str. Column name to group by
    agg_list: list. List of strings to aggregate
    
    Returns:
    df_grouped: Dataframe. Grouped Dataframe
    
    """
    df = df[[column, time]]
    df_grouped = df.groupby(group_column).agg(
        agg_list).reset_index()
    df_grouped.columns = [time] + agg_list
    return df_grouped