class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        idx= 0
        length = len(chars)

        while idx < length:
            character = chars[idx]
            count = 0

            while idx<length and character == chars[idx]:
                idx+= 1
                count += 1

            chars[writer] = character
            writer += 1

            if count > 1:
                for digit in str(count):
                    chars[writer] = digit
                    writer += 1

        return writer