
def hashAnagram(string: str):
    return "".join(sorted(string))


def groupAnagrams(anagrams: list):

    result = []
    myMap = {}

    for anagram in anagrams:
        hashKey = hashAnagram(anagram)

        if hashKey in myMap:
            myMap[hashKey].append(anagram)
        else:
            myMap[hashKey] = [anagram]

    for value in myMap.values():
        result.append(value)

    return result


if __name__ == "__main__":
    anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(anagrams))
