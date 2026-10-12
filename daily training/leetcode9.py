class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            ch = chars[read]
            count = 0

            # contar la racha del mismo caracter
            while read < n and chars[read] == ch:
                read += 1
                count += 1

            # escribir el caracter
            chars[write] = ch
            write += 1

            # escribir los digitos del conteo si es mayor a 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write