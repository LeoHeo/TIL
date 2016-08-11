# 기본적으로 Dictionary는 Hash형태이기 때문에 순서가 보장되지 않는다.
# 그런데 순서대로 저장된 Dict가 필요하다면?
# OrderedDict를 이용하면 된다.

from collections import OrderedDict

sample_dict = OrderedDict()
sample_dict["A"] = 100
sample_dict["B"] = 200
sample_dict["C"] = 300

for key, value in sample_dict.items():
    print(key, value)


# 일반적인 Dict는 값이 같으면 True를 반환하는데
# OrderedDict은 어떻게 될까?

test = dict()
test["A"] = 100
test["B"] = 200
test["C"] = 300

test2 = dict()
test2["A"] = 100
test2["B"] = 200
test2["C"] = 300

print(test["A"] == test["A"]) # True


sample_dict2 = OrderedDict()
sample_dict2["B"] = 100
sample_dict2["A"] = 200
sample_dict2["C"] = 300

# sample_dict2를 만들어서 실험해보자.
# 모든건 다 같은상황이고 OrderedDict를 썼다는점만 다르다. 
# sample_dict들은 OrderedDict라는점이다.

print(sample_dict["A"] == sample_dict2["A"]) # False

# 왜 False가 나오는가?
# sample_dict["A"]랑 sample_dict2["A"] 둘다 200이 들어있는데?

# 여기서 OrderedDict의 주된 특성이 나오는데
# OrderedDict는 Value뿐만 아니라 저장순서도 판단하기 때문에 False가 나온다.


print(sample_dict["C"] == sample_dict2["C"]) # True

# 위의 경우는 C의 Value가 300이고, 둘다 3번째이기때문에 True가 나온다.
