def seq_forw_select(features, max_k, criterion_func, print_steps=False):
    """
    Implementation of a Sequential Forward Selection algorithm.
    
    Keyword Arguments:
        features (list): The feature space as a list of features.
        max_k: Termination criterion; the size of the returned feature subset.
        criterion_func (function): Function that is used to evaluate the
            performance of the feature subset.
        print_steps (bool): Prints the algorithm procedure if True.
    
    Returns the selected feature subset, a list of features of length max_k.

    """

    # Initialization
    feat_sub = []
    k = 0
    d = len(features)
    if max_k > d:
        max_k = d

    while True:

        # Inclusion step
        if print_steps:
            print('\nInclusion from feature space', features)
        crit_func_max = criterion_func(feat_sub + [features[0]])
        best_feat = features[0]
        for x in features[1:]:
            crit_func_eval = criterion_func(feat_sub + [x])
            if crit_func_eval > crit_func_max:
                crit_func_max = crit_func_eval
                best_feat = x
        feat_sub.append(best_feat)
        if print_steps:
            print('include: {} -> feature subset: {}'.format(best_feat, feat_sub))
        features.remove(best_feat)

        # Termination condition
        k = len(feat_sub)
        if k == max_k:
            break

    return feat_sub
    

from copy import deepcopy


def seq_backw_select(features, max_k, criterion_func, print_steps=False):
    """
    Implementation of a Sequential Backward Selection algorithm.
    
    Keyword Arguments:
        features (list): The feature space as a list of features.
        max_k: Termination criterion; the size of the returned feature subset.
        criterion_func (function): Function that is used to evaluate the
            performance of the feature subset.
        print_steps (bool): Prints the algorithm procedure if True.
        
    Returns the selected feature subset, a list of features of length max_k.

    """
    # Initialization
    feat_sub = deepcopy(features)
    k = len(feat_sub)
    i = 0

    while True:

        # Exclusion step
        if print_steps:
            print('\nExclusion from feature subset', feat_sub)
        worst_feat = len(feat_sub)-1
        worst_feat_val = feat_sub[worst_feat]
        crit_func_max = criterion_func(feat_sub[:-1])

        for i in reversed(range(0,len(feat_sub)-1)):
            crit_func_eval = criterion_func(feat_sub[:i] + feat_sub[i+1:])
            if crit_func_eval > crit_func_max:
                worst_feat, crit_func_max = i, crit_func_eval
                worst_feat_val = feat_sub[worst_feat]
        del feat_sub[worst_feat]
        if print_steps:
            print('exclude: {} -> feature subset: {}'.format(worst_feat_val, feat_sub))

        # Termination condition
        k = len(feat_sub)
        if k == max_k:
            break

    return feat_sub
