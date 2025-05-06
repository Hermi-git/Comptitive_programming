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

        email_to_acc = {}
        for idx, val in enumerate(accounts):
            for email in val[1:]:
                if email in email_to_acc:
                    union(idx, email_to_acc[email])
                else:
                    email_to_acc[email] = idx
        emailmerge = defaultdict(list)
        for email, idx in email_to_acc.items():
            par = find(idx)
            emailmerge[par].append(email)

        answer = []
        for i, emails in emailmerge.items():
            name = accounts[i][0]
            answer.append([name] + sorted(emailmerge[i]))
        return answer

                


       