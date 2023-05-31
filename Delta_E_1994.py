
import math

def Delta_E_1994 ( CIE_L1, CIE_a1, CIE_b1, CIE_L2, CIE_a2, CIE_b2 ):
    WHT_L = 1
    WHT_C = 1
    WHT_H = 1
    xC1 = math.sqrt( ( CIE_a1 ** 2 ) + ( CIE_b1 ** 2 ) )
    xC2 = math.sqrt( ( CIE_a2 ** 2 ) + ( CIE_b2 ** 2 ) )
    xDL = CIE_L2 - CIE_L1
    xDC = xC2 - xC1
    xDE = math.sqrt( ( ( CIE_L1 - CIE_L2 ) * ( CIE_L1 - CIE_L2 ) )
            + ( ( CIE_a1 - CIE_a2 ) * ( CIE_a1 - CIE_a2 ) )
            + ( ( CIE_b1 - CIE_b2 ) * ( CIE_b1 - CIE_b2 ) ) )

    xDH = ( xDE * xDE ) - ( xDL * xDL ) - ( xDC * xDC )
    if ( xDH > 0 ):
        xDH = math.sqrt( xDH )
    else:
        xDH = 0

    xSC = 1 + ( 0.045 * xC1 )
    xSH = 1 + ( 0.015 * xC1 )
    xDL /= WHT_L
    xDC /= WHT_C * xSC
    xDH /= WHT_H * xSH

    Delta_E_1994 = math.sqrt( xDL ** 2 + xDC ** 2 + xDH ** 2 )

    return Delta_E_1994