def convert_organ_conc(C, organ):
    """
    :param C: Total AP concentration
    :param organ: either blood or tissue
    :return: returns IU/mm^3
    """
    if organ == 'tissue':
        d = 1.0599  # g/cm^3
        return C * d /80.
    elif organ == 'blood':
        d = 1.0428  # g/cm^3
        return C * d /5.
        # return C * d / (5. * 1e6)


def convert_AP(C, APtype, organ):
    """
    Converts the concentration of Alkaline Phosphatase from IU to mm^3/L. We assume that C refers to the entire
    concentration C in the body, which shall further be divided by 80 kg.

    ref: http://www.physiologyweb.com/calculators/units_per_volume_solution_concentration_calculator.html
    C=Ax(m/v) where C=U/L and A=U/mg. Therefore m/v = (U/L)/(U/mg) which gives mg/L
    In order to convert mg/L to cells/mm^3, I can convert mg to moles (by using the molecular mass of
    Alkaline Phosphatase which is roughly 160kDa), then finally to "cells". Liter is easily converted to mm^3.

    returns: cells/mm^3
    """
    C = convert_organ_conc(C, organ)
    if APtype == 'supp': A = 2000.
    elif APtype == 'endo': A = 1000.
    return (C * 6.02 * 10 ** 23) / (160e12*A)


def reverse_organ_conc(C, organ):
    """
    :param C: AP in IU/mm^3
    :param organ:
    :return: AP in IU/L, this is under the assumption that one needs to display the concentrations based on a /L
             basis
    """
    if organ == 'tissue':
        d = 1.0599  # g/cm^3
    elif organ == 'blood':
        d = 1.0428  # g/cm^3
    return C/d


def reverse_AP(C, APtype, organ):
    """
    :param C: AP in cells/mm^3 that is already divided by 80 kg
    :param APtype:
    :param organ:
    :return: AP in IU
    """
    if APtype == 'supp':
        A = 2000
    elif APtype == 'endo':
        A = 1000
    return reverse_organ_conc(C * 160e12 * A / (6.02 * 10 ** 23), organ)