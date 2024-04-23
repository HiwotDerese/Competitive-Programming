class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip4 = queryIP.split(".")
        ip6 = queryIP.split(":")

        def isIp4(ip):
            if len(ip) != 4:
                return False

            for x in ip:
                if not x:
                    return False

                if not x.isdigit():
                    return False

                num = int(x)
                if (not 0 <= num <= 255) or len(str(num)) != len(x):
                    return False

            return True

        def isIp6(ip):
            if len(ip) < 8:
                return False

            for x in ip:
                if not x:
                    return False

                if not 1 <= len(x) <= 4:
                    return False

                for char in x:
                    if not char.isdigit():
                        char = char.lower()
                        if ord(char) - 97 >= 6:
                            return False
 
            return True

        if len(ip4) == 4 and isIp4(ip4):
            return "IPv4"
        
        if len(ip6) == 8 and isIp6(ip6):
            return "IPv6"

        return "Neither"