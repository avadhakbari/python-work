# Write a Python script to concatenate following dictionaries to create a new one

#usng update method
# dic1 = {"name" : "avadh", "age" : 18}
# dic2 = {"city" : "surat", "pin" : 965006}
# dic3 = {}

# for i in (dic1,dic2):
#     dic3.update(i)

# print("concatenate dictionary :- ",dic3)

#using zip method
dic1 = {"name" , "age" , 'city'}
dic2 = {"avadh", 18,"surat"}
dic3 = {}

dic3 =dict(zip(dic1, dic2))
print(dic3)


