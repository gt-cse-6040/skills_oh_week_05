def check_dicts_match(d1, d2, tol=0):
    try:
        assert set(d1.keys()) == set(d2.keys())
        for k in d1:
            if type(d1[k]) is dict and type(d2[k]) is dict:
                assert check_dicts_match(d1[k], d2[k])
            assert is_close(d1[k],d2[k], tol)
    except AssertionError:
        return False
    return True


# Depricated - Do not use in new code
# 
# Use numpy.allclose instead - will disable in future updates after fixing reliant code.
def is_close(a, b, tol):
    if type(a) is float and type(b) is float:
        return abs(a-b) <= tol
    else:
        return a == b

def canonicalize_tibble(X, remove_index=True):
    var_names = sorted(X.columns)
    Y = X[var_names].copy()
    Y.sort_values(by=var_names, inplace=True)
    Y.reset_index(drop=remove_index, inplace=True)
    return Y

def assert_tibbles_left_matches_right(A, B, exact=False,  verbose=False):
    from pandas.testing import assert_frame_equal
    A_canonical = canonicalize_tibble(A, not verbose)
    B_canonical = canonicalize_tibble(B, not verbose)
    assert_frame_equal(A_canonical, B_canonical, check_exact=exact)

def assert_tibbles_are_equivalent(A, B, **kwargs):
    assert_tibbles_left_matches_right(A, B, **kwargs)

def compare_copies(a, b):
    from numpy import allclose
    try:
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b): return False
            return all(compare_copies(ai, bi) for ai, bi in zip(a, b))
        if isinstance(a, set) and isinstance(b, set):
            if len(a) != len(b): return False
            return not (a - b)
        if isinstance(a, dict) and isinstance(b, dict):
            if set(a.keys()) != set(b.keys()): return False
            return all(compare_copies(va, b[ka]) for ka, va in a.items())
        if isinstance(a, float) and isinstance(b, float):
            return allclose(a,b)
    except:
        return False
    return a == b