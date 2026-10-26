def sorting(l):
    result = []
    for i in l:
        if result == []:
            result.append(i)
            continue
        if i >= result[-1]:
            result.append(i)
        else:
            for j in result:
                if i < j:
                    result.insert(result.index(j), i)
                    break
    return result