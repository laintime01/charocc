# This is a character Occurrences count program


def check_occ(word):
    count = {}
    for x in word:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    print(count)
    return count


if __name__ == '__main__':
    word_input = input('plz input a word')
    check_occ(word_input)
