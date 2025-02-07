_WREG = "WREG"
_FREG = "FREG"

def ADDFSR(value, fsr = 0):
    output = 0x0000
    output |= 0b1110100000000000
    if fsr == 1: output |= 2**6
    if fsr == 2: output |= 2**7
    if value < 64:
        output |= value
    return output.to_bytes(2, "big")
    
def ADDLW(value): #Add literal+WREG
    output = 0x0000
    output |= 0b0000111100000000
    output |= value
    return output.to_bytes(2, "big")

def ADDWF(value, destination = _FREG, accessRAM = False): #Add WREG+File Register
    output = 0x0000
    output |= 0b0010010000000000
    if destination: output |= 0b0000001000000000
    if accessRAM: output |= 0b0000000100000000
    output |= value
    return output.to_bytes(2, "big")
