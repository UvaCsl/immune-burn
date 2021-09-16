def to_min(t):
    set_t = set_time(t, time)
    if time == 'sec':
        return set_t / 60
    elif time == 'min':
        return t
    elif time == 'hours':
        return t * 60
    elif time == 'days':
        return t * 1440


def pre_vectorfield(w, params):
    N_R, AP_Eblood, AP_Etissue, AP_Eliver, AP_Sblood, AP_Stissue, ITMb, ITM, M_R, M_A, CH, N_A, ND_A, ACH, ND_N, C_blood, C, TGF_beta = w
    if params['case'] == 0:
        N_R = AP_Eblood = AP_Etissue, AP_Eliver = AP_Sblood = AP_Stissue = M_R = M_A = CH = N_A = ND_A = ACH = ND_N = 0
    elif params['case'] == 1:
        AP_Eblood = AP_Etissue = AP_Eliver = AP_Sblood = AP_Stissue = CH = ACH = 0
    elif params['case'] == 2:
        AP_Eblood = AP_Etissue = AP_Eliver = AP_Sblood = AP_Stissue = 0
    elif params['case'] == 3:
        AP_Eblood = AP_Etissue = AP_Eliver = AP_Sblood = AP_Stissue = 0
    elif params['case'] == 4:
        AP_Eblood = AP_Etissue = AP_Eliver = AP_Sblood = AP_Stissue = 0
    elif params['case'] == 4.5:
        AP_Eblood = AP_Etissue = AP_Sblood = AP_Stissue = 0
    elif params['case'] == 5:
        AP_Sblood = AP_Stissue  = 0
    return [N_R, AP_Eblood, AP_Etissue, AP_Eliver, AP_Sblood, AP_Stissue, ITMb, ITM, M_R, M_A, CH, N_A, ND_A, ACH, ND_N, C_blood, C, TGF_beta]


def post_vectorfield(f, w, params):
    _w = place_finder(w)
    N_R, AP_Eblood, AP_Etissue, AP_Eliver, AP_Sblood, AP_Stissue, ITMb, ITM, M_R, M_A, CH, N_A, ND_A, ACH, ND_N, C_blood, C, TGF_beta = _w
    if params['case'] == 0:
        f[N_R] = f[AP_Eblood] = f[AP_Etissue] = f[AP_Eliver] = f[AP_Sblood] = f[AP_Stissue] \
            = f[ITMb] = f[ITM] = f[M_R] = f[M_A] = f[CH] = f[N_A] = f[ND_A] = f[ACH] = f[ND_N] = 0
    elif params['case'] == 1:
        f[AP_Eblood] = f[AP_Etissue] = f[AP_Eliver] = f[AP_Sblood] = f[AP_Stissue] = f[CH] = f[ACH] = 0
    elif params['case'] == 2:
        f[AP_Eblood] = f[AP_Etissue] = f[AP_Eliver] = f[AP_Sblood] = f[AP_Stissue] = 0
    elif params['case'] == 3:
        f[AP_Eblood] = f[AP_Etissue] = f[AP_Eliver] = f[AP_Sblood] = f[AP_Stissue] = 0
    elif params['case'] == 4:
        f[AP_Eblood] = f[AP_Etissue] = f[AP_Eliver] = f[AP_Sblood] = f[AP_Stissue] = 0
    elif params['case'] == 4.5:
        f[AP_Eblood] = f[AP_Etissue] = f[AP_Sblood] = f[AP_Stissue] = 0
    elif params['case'] == 5:
        f[AP_Sblood] = f[AP_Stissue] = 0
    return f


def place_finder(w):
    _w = []
    for i in range(len(w)):
        _w.append(i)
    return _w