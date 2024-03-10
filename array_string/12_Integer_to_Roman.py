class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_ = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M'
        }

        res = ''
        s_str=str(num)
        i = 0

        while i<= len(s_str)-1:
            current_symbol = s_str[i]
            current_symbol_order = len(s_str)-1-i
            current_symbol_order_value = 10**current_symbol_order

            current_symbol_with_order = str(int(current_symbol)*current_symbol_order_value)

            if num in dict_:
                return dict_[num]
            elif current_symbol_with_order == '4':
                res += 'IV'
                i += 1
            elif current_symbol_with_order == '9':
                res += 'IX'
                i += 1
            elif current_symbol_with_order == '40':
                res += 'XL'
                i += 1
            elif current_symbol_with_order == '90':
                res += 'XC'
                i += 1
            elif current_symbol_with_order == '400':
                res += 'CD'
                i += 1
            elif current_symbol_with_order == '900':
                res += 'CM'
                i += 1
            else:
                if int(current_symbol)<5 and int(current_symbol)>0:
                    res+=dict_[current_symbol_order_value]*int(current_symbol)
                    i+=1
                elif int(current_symbol)>5 and int(current_symbol)<10:
                    res += dict_[5*current_symbol_order_value]
                    res += dict_[current_symbol_order_value]*(int(current_symbol)-5)
                    i += 1
                elif int(current_symbol)!=0:
                    res += dict_[int(current_symbol_with_order)]
                    i += 1
                else:
                    i += 1
        return res


print(Solution().intToRoman(20))
