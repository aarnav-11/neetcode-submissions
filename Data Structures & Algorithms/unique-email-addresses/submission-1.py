class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        total = set()
        for email in emails:
            atPos = 0
            atPlus = -1
            for i in range(len(email)):
                if email[i] == "@":
                    atPos = i
            for i in range(len(email)):
                if email[i] == "+":
                    atPlus = i
                    break
            domain = email[atPos+1:]
            local = email[:atPos]
            print(local)
            
            if atPlus != -1:
                local = local[:atPlus-1]

            local = local.replace(".", "")
            
        
            
            total.add(local+domain)
            print(local+domain)
        return len(total)

                    