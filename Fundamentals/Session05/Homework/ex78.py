def remove_dollar_sign (s):
    s_remove = s.replace("$","")
    return s_remove
n = input("nhap vao ky tu : ")
print("chuoi sau khi bo ky tu :",remove_dollar_sign(n))
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
