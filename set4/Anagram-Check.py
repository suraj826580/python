

# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"


def check_anagram(word1, word2):
    newWord1 = "".join(sorted(word1))
    newWord2 = "".join(sorted(word2))
    if (newWord1 == newWord2):
        return True
    else:
        return False


ans = check_anagram("cinema", "iceman")
print(ans)
