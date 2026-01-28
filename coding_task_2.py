import os

def CMDOpen(name, colour):
    ## assign colour scheme from second input ##
    if colour == "greyblack":
        colourhash = "08"
    elif colour == "yellowblue":
        colourhash = "16"
    else:
        colourhash = "00"
    ## run cmd with selected name and then perform colour scheme change ##
    os.system(f'start "{name}" cmd.exe /k Color {colourhash}')

if __name__ == '__main__':
    ## enter name as string followed by "greyblack" or "yellowblue" for colour scheme ##
    CMDOpen("jack", "greyblack")
