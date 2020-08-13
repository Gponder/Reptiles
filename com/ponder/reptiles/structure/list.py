complexList = ['a', 1, 'c']
print(type(complexList))
print(complexList[0])
print(complexList[-3])
complexList = complexList+complexList
print(len(complexList))
complexList.append('abc')
print(complexList[len(complexList)-1])
del complexList[0]
print(complexList[0])
