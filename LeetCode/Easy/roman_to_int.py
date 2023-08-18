def romanToInt(s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        if len(s) == 0:
            return result
        elif len(s) == 1:
            return values.get(s)
        i = 0
        while i < len(s) - 1:
            if values.get(s[i]) >= values.get(s[i + 1]):
                result += values.get(s[i])
            else:
                result += values.get(s[i + 1]) - values.get(s[i])
                i += 1
            i += 1
        if values.get(s[-2]) >= values.get(s[-1]):
            result += values.get(s[-1])
        return result
