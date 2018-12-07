def doClothing(Length, Height):
    Clothing = []
    for cloth1 in range(0, Length+1):
        Clothing.append([])
        for cloth2 in range(0, Height+1):
            Clothing[cloth1].append(".")
    return Clothing

def doPatches(SantaCloth, patches):
    for patch in patches:
        for seam1 in range(patches[patch]["Top"], patches[patch]["Top"]+patches[patch]["Height"]):
            for seam2 in range(patches[patch]["Left"], patches[patch]["Left"]+patches[patch]["Length"]):
                if SantaCloth[seam1][seam2] == ".":
                    SantaCloth[seam1][seam2] = str(patch)
                else:
                    patches[patch]["DoesOverlap"] = True
                    try:
                        patches[int(SantaCloth[seam1][seam2])]["DoesOverlap"] = True
                    except:
                        pass
                    SantaCloth[seam1][seam2] = "#"
    return SantaCloth, patches
def overlappingArea(SantaCloth):
    Area = 0
    for seam1 in range(len(SantaCloth[0])):
        for seam2 in range(len(SantaCloth)):
            if SantaCloth[seam2][seam1] == "#":
                Area += 1
    return Area

def run(file_name):
    file = open(file_name, "r")
    patches = {}
    MaxLength = 0
    MaxHeight = 0
    for claim in file:
        claim = claim.split(" ")
        claimId = int(claim[0][1:])
        claimSpacing = claim[2].split(",")
        claimSpacing[1] = claimSpacing[1][:len(claimSpacing[1])-1]
        claimLeft = int(claimSpacing[0])
        claimTop = int(claimSpacing[1])
        claimSpacing = claim[3].split("x")
        claimLength = int(claimSpacing[0])
        claimHeight = int(claimSpacing[1])
        patches[claimId] = {}
        patches[claimId]["Top"] = claimTop
        patches[claimId]["Left"] = claimLeft
        patches[claimId]["Length"] = claimLength
        patches[claimId]["Height"] = claimHeight
        patches[claimId]["DoesOverlap"] = False
        if MaxLength < claimLeft + claimLength:
            MaxLength = claimLeft + claimLength
        if MaxHeight < claimTop + claimHeight:
            MaxHeight = claimTop + claimHeight

    SantaCloth = []
    SantaCloth = doClothing(MaxLength, MaxHeight)
    
    SantaCloth, patches = doPatches(SantaCloth, patches)

    for patch in patches:
        if patches[patch]["DoesOverlap"] == False:
            print(patch)
    
if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
