import re

pattern = re.compile(" - ")
result = pattern.sub( "*","hello - aoeu")
print(result)


