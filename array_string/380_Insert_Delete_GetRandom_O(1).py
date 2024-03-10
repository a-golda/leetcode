import random
#
# class RandomizedSet(object):
#     def __init__(self):
#         self.dict = {}
#         self.len_dict = 0
#
#     def insert(self, val):
#         """
#         :type val: int
#         :rtype: bool
#         """
#         if val in self.dict.keys():
#             return False
#         else:
#             self.dict[val] = val
#             self.len_dict+=1
#             return True
#
#     def remove(self, val):
#         """
#         :type val: int
#         :rtype: bool
#         """
#         if val not in self.dict.keys():
#             return False
#         else:
#             del self.dict[val]
#             self.len_dict -=1
#             return True
#
#     def getRandom(self):
#         """
#         :rtype: int
#         """
#         return random.choice(self.dict.keys())


import random

class RandomizedSet(object):
    def __init__(self):
        self.dict_ = {}
        self.list_ = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict_:
            self.dict_[val] = len(self.list_)
            self.list_.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict_:
            return False
        else:
            idx = self.dict_[val]
            self.dict_[self.list_[-1]] = idx
            self.list_[-1], self.list_[idx] = self.list_[idx], self.list_[-1]
            self.list_.pop()
            self.dict_.pop(val)
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list_)


obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()


print([param_1, param_2, param_3])