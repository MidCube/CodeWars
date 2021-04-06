def binary_array_to_number(arr):
  strArr = ""
  for item in arr:
        strArr+=str(item)
  return int(strArr,2)
