# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = [i for i in range(len(accounts)+1)]
        rank = [0] * (len(accounts)+1)
    
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                rankx = rank[rootx]
                ranky = rank[rooty]
                if rankx > ranky:
                    root[rooty] = rootx
                elif rankx < ranky:
                    root[rootx] = rooty
                else:
                    root[rooty] = rootx
                    rank[rootx] += 1
        
        email_to_person = {}
        for index, value in enumerate(accounts):
            for email in value[1:]:
                if email in email_to_person:
                    union(index, email_to_person[email])
                else:
                    email_to_person[email] = index
        print(email_to_person)
        
        account_merge = defaultdict(list)
        for email, person in email_to_person.items():
            parent = find(person)
            account_merge[parent].append(email)
            
        print(account_merge)
        result = []
        for parent, acc in account_merge.items():
            person = accounts[parent][0]
            result.append([person] + sorted(acc))


        return result 
