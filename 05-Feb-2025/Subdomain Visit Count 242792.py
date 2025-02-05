# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdomains_dict = defaultdict(int)
        for cpdomain in cpdomains:
            visited, domains = cpdomain.split()
            visited = int(visited)

            subdomains = domains.split(".")

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                cpdomains_dict[subdomain] += visited

        result = []
        for subdomain, visited in cpdomains_dict.items():
            result.append(str(visited) + " " + subdomain)
        
        return result



