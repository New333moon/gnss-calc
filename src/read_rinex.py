#sat_id = "G08"

def read_rinex_nav(filename, sat_id):

    with open(filename, 'r') as f:
        lines = f.readlines()

    i = 0
    while "END OF HEADER" not in lines[i]:
        i += 1
    i += 1

    while i < len(lines):

        if lines[i].startswith(sat_id):

            l1 = lines[i]
            l2 = lines[i+1]
            l3 = lines[i+2]
            l4 = lines[i+3]
            l5 = lines[i+4]
            l6 = lines[i+5]
            l7 = lines[i+6]

            params = {}

            # -------- line1 ----------
            params["year"]   = int(l1[4:8])
            params["month"]  = int(l1[9:11])
            params["day"]    = int(l1[12:14])
            params["hour"]   = int(l1[15:17])
            params["minute"] = int(l1[18:20])
            params["second"] = int(float(l1[20:23]))

            params["af0"] = float(l1[23:42])
            params["af1"] = float(l1[42:61])
            params["af2"] = float(l1[61:80])

            # -------- line2 ----------
            params["IODE"]   = float(l2[4:23])
            params["Crs"]    = float(l2[23:42])
            params["deltan"] = float(l2[42:61])
            params["M0"]     = float(l2[61:80])

            # -------- line3 ----------
            params["Cuc"]   = float(l3[4:23])
            params["e"]     = float(l3[23:42])
            params["Cus"]   = float(l3[42:61])
            params["sqrtA"] = float(l3[61:80])

            # -------- line4 ----------
            params["toe"]    = float(l4[4:23])
            params["Cic"]    = float(l4[23:42])
            params["Omega0"] = float(l4[42:61])
            params["Cis"]    = float(l4[61:80])

            # -------- line5 ----------
            params["i0"]       = float(l5[4:23])
            params["Crc"]      = float(l5[23:42])
            params["omega"]    = float(l5[42:61])
            params["Omegadot"] = float(l5[61:80])

            # -------- line6 ----------
            params["idot"] = float(l6[4:23])

            return params

        i += 8   

    raise ValueError("Satellite not found")

