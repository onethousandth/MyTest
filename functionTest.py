
import math

flt_a = 2
flt_b = 3
flt_c = 1

flt_returnX = 0
flt_returnY = 0
bl_NotNumber = False


def quadratic(flt_a, flt_b, flt_c, flt_returnX, flt_returnY, bl_NotNumber):
    if flt_b*flt_b-4*flt_a*flt_c >= 0:
        bl_NotNumber = True
        flt_returnX = (-flt_b+math.sqrt(flt_b*flt_b-4*flt_a*flt_c))/2
        flt_returnY = (-flt_b-math.sqrt(flt_b*flt_b-4*flt_a*flt_c))/2
        return flt_returnX, flt_returnY, bl_NotNumber
    else:
        bl_NotNumber = False
        flt_returnX = "-i"
        flt_returnY = "-i"
        return flt_returnX, flt_returnY, bl_NotNumber


flt_returnX, flt_returnY, bl_NotNumber = quadratic(
    flt_a, flt_b, flt_c, flt_returnX, flt_returnY, bl_NotNumber)

print('{:.4f}'.format(flt_returnX), '\t{:.4f}'.format(
    flt_returnY), '\t{}'.format(bl_NotNumber))

print('{:+.4f}\t\t{:+.4f}\t\t{}'.format(flt_returnX, flt_returnY, bl_NotNumber))
