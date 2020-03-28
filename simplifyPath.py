def simplifyPath(path):
    pathList = path.split('/')
    result = []
    for item in pathList:
        if item == '.':
            continue
        if item == '..':
            if result:
                result.pop()
        elif item:
            result.append(item)
    return '/' + '/'.join(result)
