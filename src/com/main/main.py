from src.com.main.JsonParser import JsonParser
from src.com.main.LogParser import LogParser

fileLocation = "C:/Users/kyeongrok.kim/Desktop/"
fromFileName = "parse.log"
targetFileName = "141000-1704623.txt"
pattern = '2017-06-08 14:[1-2][1-9]:[0-9][0-9].*startTimestamp.*1704623.*'

logParser = LogParser(fileLocation, fromFileName, targetFileName)
logParser.extractPattern(pattern)
logParser.replaePattern(targetFileName, "json.txt"
                     , "2017-06-08 14:[1-2][1-9]:[0-9][0-9].*- {", "{")

jsonParser = JsonParser(fileLocation)
jsonParser.readFiles("json.txt")


