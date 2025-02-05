# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = Counter()
        for domain in cpdomains:
            splitted = domain.split()
            count = int(splitted[0])
            domains = splitted[1].split(".")
            for i in range(len(domains)): 
                ans[".".join(domains[i:])] += count

        return [f'{cnt} {domain}' for domain,cnt in ans.items()]   