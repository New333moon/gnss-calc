import math

def sat_pos(params,hour, minute, second):
    
    time = hour * 3600 + minute * 60 + second
    
    #statics:
    miu = 3.986004418e14