## surrogate key
> 디비에서 각row의 ID에 해당하는 primary key는 비지니스 관련 의미가 전혀 없는 surrogate key (대부분의 경우 디비에서 증가 시켜주는 숫자만으로 된 키를 사용)를 사용하고 object레벨의 ID는 business key를 사용하시는게 좋다. (예. DB와 상관 없지만 비지니스 로직상 의미가 있는 인보이스 넘버, 오더 넘버 등등)
