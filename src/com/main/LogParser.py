import re

class LogParser:
    def extractPattern(self, sFileLocation, sFromFileName, sTargetFileName, sPattern):
        with open(sFileLocation + sFromFileName, mode="rt", encoding='utf-8') as f:
            string = f.read()

        pattern = re.compile(sPattern)
        findAll = pattern.findall(string)

        print(type(findAll))
        print(len(findAll))

        file = open(sFileLocation + sTargetFileName, mode="w", encoding='utf-8')
        for item in findAll:
                print(item.__sizeof__())
                file.write(item + "\n")
        file.close()
        print("success")

fileLocation = "C:/Users/kyeongrok.kim/Desktop/"
fileName = "parse_2017-06-05.43.log"
targetFileName = "1703427.txt"
pattern = '.*1703427.*'

parser = LogParser()
parser.extractPattern(fileLocation, fileName, targetFileName, pattern)




