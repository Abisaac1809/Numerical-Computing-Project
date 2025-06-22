class Conversor:
    @staticmethod
    def convertToDecimal(number: str, base: int) -> float:
        digits = "0123456789ABCDEF"
        number = number.upper()

        if '.' in number:
            integerPart, fractionPart = number.split('.')
        else:
            integerPart, fractionPart = number, ''


        decimal = 0
        for i, char in enumerate(integerPart[::-1]):
            if char not in digits[:base]:
                raise ValueError(f"Dígito inválido: {char} para base {base}")
            decimal += digits.index(char) * (base ** i)


        for i, char in enumerate(fractionPart, start=1):
            if char not in digits[:base]:
                raise ValueError(f"Dígito inválido: {char} para base {base}")
            decimal += digits.index(char) * (base ** -i)

        return decimal