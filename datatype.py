a = 100 # 정수 (int)
b = 3.1415 # 실수 (float)
c = 'Python' # 문자열 (str)
d = True # T or F (bool)
print(a, type(a)) # type은 해당 변수의 자료형(datatype)을 보여준다
print(b, type(b))
print(c, type(c))
print(d, type(d))

colors = ['빨', '주', '노', '초', '파'] # 리스트 (list)(가변형)
weekday = ('월', '화', '수') # 튜플 (tuple)(불변형)
students = {'혜민':'131-9898', '서준':'457-4777'} # 딕셔너리(dict)(가변형)
print(type(colors), type(weekday), type(students))


"""
변수는 한번에 한개의 값만 저장한다. 그래서 이미 저장된값이 있는 변수에 새로운 값을 저장하면 기존에 있던 값은 지워지고 새로운 값이 저장되고 새로운 자료형으로 변경된다
"""
A = 100
print(A, '을 저장했을때 A의 자료형', type(a))
A = 'Python'
print(A, '을 저장했을때 A의 자료형', type(a))

