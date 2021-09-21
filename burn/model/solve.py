
def get_init(w0, params):
    """
    Sets the initial conditions based on the assigned case.

    Arguments:
        w0       :  vector of the initial conditions
    """
    N_R0, AP_Eb0, AP_Et0, AP_El0, AP_S0, AP_St0, ITMb0, ITM0, M_R0, M_A0, CH0, N_A0, ND_A0, ACH0, ND_N0, C_blood0, C0, C_A0, C_B0, TGF_beta0 = w0

    if params['case'] == 0:
        N_R0 = AP_Eb0 = AP_Et0 = AP_El0 = AP_S0 = AP_St0 = M_R0 = M_A0 = CH0 = N_A0 = ND_A0 = ACH0 = ND_N0 = 0
    elif params['case'] == 1:
        AP_Eb0 = AP_Et0 = AP_El0 = AP_S0 = AP_St0 = CH0 = ACH0 = 0
    elif params['case'] == 2:
        AP_Eb0 = AP_Et0 = AP_El0 = AP_S0 = AP_St0 = 0
    elif params['case'] == 3:
        AP_Eb0 = AP_Et0 = AP_El0 = AP_S0 = AP_St0 = 0
    elif params['case'] == 4:
        AP_Eb0 = AP_Et0 = AP_El0 = AP_S0 = AP_St0 = 0
    elif params['case'] == 4.5:
        AP_Eb0 = AP_Et0 = AP_S0 = AP_St0 = 0
    elif params['case'] == 5:
        AP_S0 = AP_St0 = 0
    w0 = [N_R0, AP_Eb0, AP_Et0, AP_El0, AP_S0, AP_St0, ITMb0, ITM0, M_R0, M_A0, CH0, N_A0, ND_A0, ACH0, ND_N0, C_blood0, C0, C_A0, C_B0, TGF_beta0]
    return w0