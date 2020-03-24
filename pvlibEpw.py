from pvlib.iotools import read_epw


epwData=read_epw(r"assets/mannheim.epw")

print(type(epwData))