import math

def Delta_E_CIE ( CIE_L1, CIE_a1, CIE_b1, CIE_L2, CIE_a2, CIE_b2 ):
    Delta_E = math.sqrt( ( ( CIE_L1 - CIE_L2 ) ** 2 )
               + ( ( CIE_a1 - CIE_a2 ) ** 2 )
               + ( ( CIE_b1 - CIE_b2 ) ** 2 ) )
    
    return Delta_E