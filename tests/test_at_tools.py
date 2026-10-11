from at_tools import at_fraction 
 
def test_at_fraction_half(): 
    """Two of the four bases are A or T.""" 
    assert at_fraction("ATGC") == 0.5
