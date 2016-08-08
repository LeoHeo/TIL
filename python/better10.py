# 현재 아이템의 인덱스를 알고 싶을때 아래와 같이 코딩한다.

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print("{i} : {flavor}".format(
        i=i,
        flavor=flavor,
    ))


# 근데 위의 코드는 별로 파이써닉하지 않다.
# 내장함수 enumerate 사용
for i, flavor in enumerate(flavor_list):
    print("{i} : {flavor}".format(
        i=i,
        flavor=flavor,
    ))

# 시작할 인덱스 번호를 지정할수도 있다.
for i, flavor in enumerate(flavor_list, 1):
    print("{i} : {flavor}".format(
        i=i,
        flavor=flavor,
    ))
