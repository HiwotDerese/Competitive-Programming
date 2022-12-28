if __name__ == '__main__':
    n = int(input())
    elts = map(lambda a: int(a), input().split())
    tpl = tuple(elts)
    print(hash(tpl))