def part(arr):
    #your code here
    result="Mine's a Pint"
    alan=["Partridge","PearTree","Chat","Dan","Toblerone","Lynn","AlphaPapa","Nomad"]
    result+="".join(["!" if item in alan else "" for item in arr])
    return result if result[-1]=="!" else "Lynn, I've pierced my foot on a spike!!"
