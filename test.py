import re
i_str = "I'm sick and hence i want sick leave"
l = ["sick", "sick leave"]
replace_word = "@entity"
# meta_data = []
sorted_list = sorted(l, key=lambda x: -len(x))
updated_list = []

for i in range(len(sorted_list)):
    updated_list.append(i)
    i_str = i_str.replace(sorted_list[i], "${"+str(i)+"}")

for i in updated_list:
    i_str = i_str.replace("${"+str(i)+"}", sorted_list[i]+replace_word)

print(i_str)
















# for i in range(len(sorted_list)-1):
#     this_word_meta = {"word": sorted_list[i]}
#     if i == 0:
#         occured_list = [index.start() for index in re.finditer(sorted_list[i], i_str)]
#         end_list = [end+len(sorted_list[i]) for end in occured_list]
#         this_word_meta.update({"occured_list": occured_list, "end_list": end_list})
#         i_str = i_str.replace(sorted_list[i], sorted_list[i]+replace_word)
#         meta_data.append(this_word_meta)
#     else:
#
#
#         pass
#
#
    # for data in meta_data:





