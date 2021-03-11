# Chapter02-1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
# 'Content', "Content"도 가능하다.
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()


# separator 옵션
# 각각의 출력 값들 사이에 sep='' 옵션을 줌으로써 사이에 해당 데이터를 넣어준다.
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='')
print()


# end 옵션
# print()의 기본 end='n' default로 들어간다.
# end=''을 해주면 default로 들어가지 않는다.
print('Welcome to', end='')
print('IT News', end=' ')
print('Web Site')
print()


# file 옵션
# file=sys.stdout은 명시해주지 않으면 default로 file=sys.stdout
# file=sys.stdout은 표준 출력장치로 내보내라는 뜻.
import sys

print('Learn Python', file=sys.stdout)
print()


# format 사용(d : 3, s : 'python', f : 3.1445454)
# % 기호를 사용하여 변수값을 출력할 수 있다.
# %d : 정수, %s : 문자열, %f : 실수
# 다만 헤딩 깂에 무엇을 넣어줘야 할지 지정해줘야 하므로 % ('one', 'two')  지정해줘야한다.
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', 'two')) # 자동으로 {0} {1}
print('{1} {0}' .format('one', 'two'))
print()

# %s
print('%10s' % ('nice')) # 왼쪽으로 여백 총 자릿수 10
print('{:>10}' .format('nice')) # 왼쪽으로 여백 총 자릿수 10

print('%-10s' % ('nice')) # 오른쪽으로 여백 총 자릿수 10
print('{:10}' .format('nice')) # 오른쪽으로 여백 총 자릿수 10

print('{:_>10}' .format('nice')) # 왼쪽으로 _ 총 자릿수 10
print('{:^10}' .format('nice')) # 중앙 정 총 자릿수 10

print('%.5s' % ('nice')) #.은 5글자로 절삭
print('%5s' % ('pythonstudy'))
print('{:10.5}' .format('pythonstudy')) # 공간은 10개지만 5개만 출력


# %d
print('%d %d' % (1,2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42))

# %f
print('%f' % (3.13132313213))
print('{:f}' .format(3.13132313213))

print('%06.2f' %(3.141592653589793)) # .포함해서 총 6자리, 소수점은 2자리
print('{:06.2f}' .format(3.141592653589793))
