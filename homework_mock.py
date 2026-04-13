# ---------------------------------------------------
# son = input("son kiriting: ")
# son_lst = list(son.split())
# son_s = sorted(son_lst)
# dct = {}
# for index, value in enumerate(son_s):
#     if value not in dct:
#         dct[value] = index
# lst = []
# for i in son_lst:
#     lst.append(dct[i])
# print(lst)

# ------------------------------------------------------
# def raqamlar_s(word):
#     s = ""
#     for char in word:
#         if char.isdigit():
#             s += char
#         else:
#             s += " "
#     s_split = s.split()
#     res = set()
#     for p in s_split:
#         res.add(int(p))
#     return len(res)
# natija = raqamlar_s("a123bc34d8ef34")
# print(natija)