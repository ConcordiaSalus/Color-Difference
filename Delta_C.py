
import math

def Delta_C ( CIE_a1, CIE_b1, CIE_a2, CIE_b2 ):
    Delta_C = math.sqrt( ( CIE_a2 ** 2 ) + ( CIE_b2 ** 2 ) ) - math.sqrt( ( CIE_a1 ** 2 ) + ( CIE_b1 ** 2 ) )

    return Delta_C
