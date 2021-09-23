def get_med_mad(cytokine, df, params, to_calculate = ['median', 'mad']):
    mw = params[cytokine]
    mult = ((1*10**-12)*(6.02*10**23)/((1*10**-3)*mw*10**6))
    df[cytokine] = df[cytokine] * mult
    df_cyto = df[[cytokine, 'Day']].groupby('Day').agg({cytokine:to_calculate})
    df_cyto.columns = df_cyto.columns.droplevel(0)
    df_cyto = df_cyto.reset_index()
    df_cyto['time'] = df_cyto.Day * 24
    df_cyto = df_cyto.drop('Day', axis=1)
    return df_cyto