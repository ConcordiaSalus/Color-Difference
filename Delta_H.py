
import math

def Delta_H ( CIE_a1, CIE_b1, CIE_a2, CIE_b2 ):
    xDE =  math.sqrt( ( CIE_a2 ** 2 ) + ( CIE_b2 ** 2 ) ) - math.sqrt( ( CIE_a1 ** 2 ) + ( CIE_b1 ** 2 ) )
    Delta_H = math.sqrt( ( CIE_a2 - CIE_a1 ) ** 2 + ( CIE_b2 - CIE_b1 ) ** 2 - ( xDE ** 2 ) )

    return Delta_H