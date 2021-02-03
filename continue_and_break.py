shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy {}".format(item))
#
# print()
#
# # this will work using continue
# for item in shopping_list:
#     if item == "spam":
#         continue
#
#     print("Buy {}".format(item))
#
# for item in shopping_list:
#     if item == "spam":
#         break
#
#     print("Buy {}".format(item))

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
print("Item found at postiton {}".format(found_at))