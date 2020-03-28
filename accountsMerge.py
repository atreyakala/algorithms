from collections import defaultdict

def accountsMerge(accounts):
    emailOwner = {}
    graph = buildEmailGraph(accounts, emailOwner)
    mergedAccounts = []
    visited = set()
    for emailId, name in emailOwner.items():
        if emailId not in visited:
            accountEmails = []
            explore(name, emailId, graph, visited, accountEmails)
            mergedAccounts.append([name] + sorted(accountEmails))
    return mergedAccounts

def explore(name, emailId, graph, visited, accountEmails):
    visited.add(emailId)
    accountEmails.append(emailId)
    for nextEmailId in graph[emailId]:
        if nextEmailId not in visited:
            explore(name, nextEmailId, graph, visited, accountEmails)

def buildEmailGraph(accounts, emailOwner):
    graph = defaultdict(lambda: [])
    for account in accounts:
        name = account[0]
        firstEmailId = account[1]
        remainingEmailIds = account[2:]
        emailOwner[firstEmailId] = name
        for emailId in remainingEmailIds:
            emailOwner[emailId] = name
            graph[firstEmailId].append(emailId)
            graph[emailId].append(firstEmailId)
    return graph
