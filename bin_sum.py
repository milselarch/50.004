class Solution:
    def to_bits(self, num):
        bit_number = [0] * 12
        is_negative = False

        if num < 0:
            num = abs(num)
            is_negative = True

        for k in range(11):
            if num % 2 == 1:
                bit_number[k] = 1

            num >>= 1

        if is_negative:
            for k in range(12):
                bit_number[k] ^= 1

        return bit_number

    @staticmethod
    def flip_bits(bit_number):
        bit_number = bit_number[::]

        for k in range(len(bit_number)):
            bit_number[k] ^= 1

        return bit_number

    def getSum(self, a: int, b: int) -> int:
        both_neg = (a < 0) and (b < 0)
        has_neg = (a < 0) or (b < 0)
        carry = int(has_neg)

        # 2**10 = 1024; 1024 > 1000
        a_bits = self.to_bits(a)
        b_bits = self.to_bits(b)
        out_bits = [0] * 12

        for k in range(12):
            a_digit = a_bits[k]
            b_digit = b_bits[k]

            digit_out = int(
                (a_digit and b_digit and carry) or
                ((not a_digit) and (not b_digit) and carry) or
                (a_digit and (not b_digit) and (not carry)) or
                ((not a_digit) and b_digit and (not carry))
            )

            carry = int(
                (a_digit and b_digit) or
                (a_digit and carry) or
                (b_digit and carry)
            )

            out_bits[k] = digit_out
            # print(k, a_digit, b_digit, digit_out, carry)
            a >>= 1
            b >>= 1

        negative_out = out_bits[-1]
        value_bits = out_bits[:-1][::]
        if negative_out:
            value_bits = self.flip_bits(value_bits)

        if both_neg:
            # print('BOTHN EG', value_bits)
            for k in range(len(value_bits)):
                if value_bits[k] == 0:
                    value_bits[k] = 1
                    continue

                value_bits[k] = 0
                break

        reverse_bits = value_bits[::-1]
        # print(f'reverse_bits={reverse_bits}')
        bin_out = '0b'.join([
            ''.join([str(x) for x in reverse_bits])
        ])

        output = int(bin_out, 2)

        if negative_out:
            output = ~output

        # print(f'NEG OUT', negative_out)
        return output


if __name__ == '__main__':
    soln = Solution()
    print(soln.getSum(25, 23))
