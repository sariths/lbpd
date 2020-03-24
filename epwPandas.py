from ladybug.epw import EPW
from pandas import DataFrame
from collections import OrderedDict

#Path to epw file.
epwCls=EPW(r"assets/mannheim.epw")

epwDataList=epwCls.to_dict()['data_collections']
epwDataDict=OrderedDict()

for dataCol in  epwDataList:
    dataName=dataCol['header']['data_type']['name']
    epwDataDict[dataName]=dataCol['values']

epwDataFrame=DataFrame(epwDataDict)


#print all available columns
#print(epwDataFrame.columns)


#Print dry bulb temperature
print(epwDataFrame["Dry Bulb Temperature"])

