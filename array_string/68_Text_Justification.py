class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        words_groups = []
        words_groups_length = []

        current_group = []
        current_group_l = 0
        for word in words:
            if current_group_l+len(word) + 1 <= maxWidth:
                current_group_l+=len(word)+1
                current_group.append(word)
            else:
                words_groups.append(current_group)
                words_groups_length.append(min(current_group_l-len(current_group), maxWidth))
                current_group = [word]
                current_group_l = len(word)

        words_groups.append(current_group)
        words_groups_length.append(min(current_group_l - len(current_group), maxWidth))


        for i in range(len(words_groups)):
            if i!=len(words_groups)-1:
                words_groups_len = len(words_groups[i])-1
                current_row = ''
                needed_whitespaces = maxWidth - words_groups_length[i]
                if words_groups_len!=0:
                    for j in range(len(words_groups[i])):
                        if j!= len(words_groups[i])-1:
                            amount_of_ws = (int(needed_whitespaces / words_groups_len) + (
                                    needed_whitespaces % words_groups_len > 0))
                            white_space = '' + ' ' * amount_of_ws
                            current_row += words_groups[i][j]
                            current_row += white_space
                            words_groups_len -=1
                            needed_whitespaces -= amount_of_ws
                        else:
                            current_row += words_groups[i][j]
                else:
                    current_row+=words_groups[i][0]+' '*needed_whitespaces
                res.append(current_row)
            else:
                needed_whitespaces = maxWidth - words_groups_length[i]
                current_row = ''
                for j in range(len(words_groups[i])-1):
                    current_row+=words_groups[i][j]+' '
                    needed_whitespaces-=1
                current_row+=words_groups[i][-1]
                current_row+=' '*needed_whitespaces
                res.append(current_row)
        return res

print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 10))


# group words into list of lists according to lines
# one more list of elements lenth of group without whitespaces
# count words in each line and define the amount of extra spaces
# if one word add all spaces to end
# if last string left-justify