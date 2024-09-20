def read(path: str):
    with open(path) as f:
        file_contents = f.read()
    return (file_contents)


def words(contents: str):
    count = []
    count = contents.split()
    return (len(count))


def char_times(contents: str):
    lower = contents.lower()
    count = {}
    for char in lower:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return (count)


def myfunc(contents):
    return contents['times']


def sort(contents: str):
    charlist = []
    # contents.split(",")
    for char in contents:
        if char.isalpha():
            charlist.append({"char": char, "times": contents[char]})
    charlist.sort(reverse=True, key=myfunc)
    return (charlist)


def main():
    path = "./books/frankenstein.txt"
    
    r = read(path)
    w = words(r)
    c = char_times(r)
    s = sort(c)

    print(f"{w} words found in the document")
    for letter in s:
        print(f"The '{letter['char']}' character was found {letter['times']} times")
    return 0


if __name__ == "__main__":
    main()
