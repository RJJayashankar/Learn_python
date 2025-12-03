text1 = "hello"
text2 = "elloh"

count_text1 = {}
count_text2 = {}

for text in text1:
    if text in count_text1:
        count_text1[text] += 1
    else:
        count_text1[text] = 1

for text in text2:
    if text in count_text2:
        count_text2[text] += 1
    else:
        count_text2[text] = 1


print(count_text1)
print(count_text2)
if count_text1 == count_text2:
    print("they are an anagram")