import re
text = "The quick brown fox jumps over the lazy dog ."

match = re.search("brown",text)
print(match)
if match:
    print("Match Found!")
    print("Start Index:",match.start())
    print("End Index:",match.end())

matches = re.findall("the",text,re.IGNORECASE)
print("Matches",matches)

new_text = re.sub("fox","cat",text)
print("new_text:",new_text)