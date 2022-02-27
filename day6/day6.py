input_data = "day6_data.txt"

# opens txt file and splits the groups based on two consecutive newlines
with open(input_data, "r") as f:
    forms = f.read().strip().split("\n\n")

clean_list = []
for form in forms:
    clean_list.append(len(set(form.replace("\n", ""))))

print("The number of questions answered with yes is: {x}".format(
    x=sum(clean_list)))
