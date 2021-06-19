"""
721. Accounts Merge https://leetcode.com/problems/accounts-merge/

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

from collections import defaultdict
from typing import List, Dict


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    email_owner_map = {}
    email_graph = build_email_graph(accounts, email_owner_map)
    merged_accounts = []
    visited = set()
    for email_id, owner_name in email_owner_map.items():
        if email_id not in visited:
            component = []
            dfs(email_id, email_graph, visited, component)
            merged_accounts.append([owner_name] + sorted(component))
    return merged_accounts


def build_email_graph(accounts: List[List[str]], email_owner_map: Dict[str, str]) -> Dict[str, List[str]]:
    graph = defaultdict(set)
    for account in accounts:
        name = account[0]
        first_email_id = account[1]
        email_owner_map[first_email_id] = name
        for email in account[2:]:
            email_owner_map[email] = name
            graph[first_email_id].add(email)
            graph[email].add(first_email_id)
    return graph


def dfs(email: str, graph: Dict[str, List[str]], visited: set, component: List[str]) -> None:
    visited.add(email)
    component.append(email)
    for next_email in graph[email]:
        if next_email not in visited:
            dfs(next_email, graph, visited, component)


# O(sum(Ai * log(Ai)) | O(sum(Ai))

'''
    Time Complexity : O( sum(Mi * log(Mi)) )
    Space Complexity : O( sum(Mi) )

    Where sum() denotes the summation and "Mi" denotes the length of accounts[i].
'''


def test_0():
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    print(accounts_merge(accounts))
