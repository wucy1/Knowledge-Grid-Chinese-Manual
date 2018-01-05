instr = {'VKORC1-1639G>A': '(+)', 'CYP2C9*2': '(-)', 'CYP2C9*3': 'POSITIVE', 'European': 'POSITIVE'}

def getGuideline(instr):
    if not instr["VKORC1-1639G>A"] or not instr["CYP2C9*2"] or not instr["CYP2C9*3"] or not instr["European"]:
        #input does not include proper allele keys
        raise Exception("Input must contain keys 'VKORC1-1639G>A' and 'CYP2C9*2' and 'CYP2C9*3' and 'European'")
    else:
        instr["VKORC1-1639G>A"]=instr["VKORC1-1639G>A"].strip()
        instr["CYP2C9*2"]=instr["CYP2C9*2"].strip()
        instr["CYP2C9*3"]=instr["CYP2C9*3"].strip()
        instr["European"]=instr["European"].strip()

    positives=("POSITIVE","(+)")
    pos1=0
    pos2=0
    pos3=0
    pos4=0

    for p_str in positives:
        if p_str in instr["VKORC1-1639G>A"]:
            pos1=1
    for p_str in positives:
        if p_str in instr["CYP2C9*2"]:
            pos2=1
    for p_str in positives:
        if p_str in instr["CYP2C9*3"]:
            pos3=1
    for p_str in positives:
        if p_str in instr["European"]:
            pos4=1
    if (pos1+pos2+pos3+pos4)==4:
        return "Calcaulate dose based on validated published pharmacogenetic algorithms"
    else:
        return "Dose clinically"

a = getGuideline(instr)
print (a)
