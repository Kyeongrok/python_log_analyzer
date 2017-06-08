import json

'''
1.파일을 읽는다.
2.읽어서 list로 만든다.
3.json을 읽는다.
4.json을 encoding한다. dict로 뽑힌다.
startTimeStamp, endTimeStamp를 뽑아서 list에 담는다.
list를 파일에 쓴다.
'''
def readFiles(sFileLocation, sFromFileName):
    with open(sFileLocation + sFromFileName, mode="rt", encoding='utf-8') as f:
        stringList = f.readlines()
        item = stringList[0]
        print(item)

        for item in stringList:
            jsonObject = json.loads(item)
            print(jsonObject['startTimestamp'] + " " + jsonObject['endTimestamp'])


fileLocation = "C:/Users/kyeongrok.kim/Desktop/"
readFiles(fileLocation, "1703427.txt")

