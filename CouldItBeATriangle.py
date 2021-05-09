s = float(input('tell me the first straight segment '))
s2 = float(input('tell me the second straight segment '))
s3 = float(input('tell me the third straight segment '))
if s < s2 + s3 and s2 < s + s3 and s3 < s + s2:
    print('It could be a triangle')
else:
    print("It coundn't be a triangle")
