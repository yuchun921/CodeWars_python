geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    ans = []
    for i in birds:
        if not i in geese:
            ans.append(i)
    return ans
