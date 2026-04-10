import json
f = open("test.json")
data = json.load(f)
# data = json.load(f)["branches"]
# for i in data["branches"]:
#     print(i['name'])


# --------------------------------------------------------------

# for i in data["branches"]:
#         for x in i['teachers']:
#                 if x['subject'] == "Python":
#                         print(x)


# --------------------------------------------------------------

# for i in data["branches"]:
#     counter = 0
#     for x in i['students']:
#         counter +=1
#     print(f"{i['name']}da {counter}ta student bor")        




# --------------------------------------------------------------


# max_payment = 0
# max_student = 0   

# for branch in data['branches']:
#     for student in branch['students']:
#         if student['payment'] > max_payment:
#             max_payment = student['payment']
#             max_student = student

# print(f"{max_student['name']}")
# print(f"{max_payment:,} so'm")


# --------------------------------------------------------------




# for branch in data['branches']:
#     jami = 0
#     for student in branch['students']:
#         jami += student['payment']

#     print(f"{branch['name']}: {jami:,} so'm")


# --------------------------------------------------------------




# for branch in data['branches']:
#     for teacher in branch['teachers']:
#         if teacher['experience'] > 5:
#             print(f"{teacher} yil")



# --------------------------------------------------------------



#7chisiga tushunmadim


f.close()
