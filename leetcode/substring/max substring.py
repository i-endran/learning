
def lengthOfLongestSubstring(s: str) -> int:
    
    result = 0
    index = {}
    l,r = 0,0

    for r, char in enumerate(s):
        if char in index and index[char] >= l:
            l = index[char] + 1

        index[char] = r
        result = max(result, r - l + 1)

        print(f"l -> {l}, r -> {r}, char -> {char}, result -> {result}    index -> {index}")
    
    return result


def main():
    length = lengthOfLongestSubstring("abcabcabbc")
    print("Length: ", length)


if __name__ == "__main__":
    main()