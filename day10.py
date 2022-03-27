#functions with outputs

#use return to have an output
# def my_function():
#     return 3 * 2

# output = my_function()

#new
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("asvinth", "RAGHuDheVAN")
print(formatted_string)

#multiple return keywords in one function
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
