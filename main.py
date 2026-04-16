from read_rinex_file import read_rinex_nav
from sat_pos import sat_pos

sat_id = "G08"
nav_file = "data/rinex/BRDM00DLR_S_20260010000_01D_MN.rnx"

a = read_rinex_nav(nav_file, sat_id)

for k,v in a.items():
    print(k,v)

    

