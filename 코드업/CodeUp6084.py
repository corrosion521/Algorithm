'''
round함수나 %.f나 일반적으로 차이가 없음
'''
h,b,c,s = map(int,input().split())

result = ((h*b*c*s)/8/1024/1024)
print("%.1f"%result,"MB")