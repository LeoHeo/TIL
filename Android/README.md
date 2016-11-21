## Android Tip

### API Level 16이하
- API Level 16이하에서는 `RelativeLayout.LayoutParams` 주의사항
- 만약 `minSdkVersion 16`이라면 `**start, **end` 옵션을 둘다 써줘야 한다.

e.g) 아래와 같이 써준다.

```
android:layout_alignParentEnd="true"
android:layout_alignParentRight="true"
```

```
android:layout_toStartOf="@id/list_item_crime_solved_check_box"
android:layout_toLeftOf="@id/list_item_crime_solved_check_box"
```

### Styles에서 Title없애고자 할때
`android:windowNoTitle`로 쓰면 작동을 안한다.

아래와 같이 써줘야 한다.

```xml
<item name="windowNoTitle">true</item>
```

### xml에서 @string(문자열 리소스)키 또는 값을 보고싶을때

- value값을 보고 싶을때 -> `cmd + -`
- key값을 보고싶을때 -> `cmd + =`

### Method에 매개변수 정보보기
- `cmd + p`를 눌러 매겨변수 정보를 볼수있다.

### [Android] getColor와 getDrawable deprecated
[참고](http://gogorchg.tistory.com/entry/Android-getColor%EC%99%80-getDrawable-deprecated)

```java

// Deprecated된 방식
//getResources().getDrawable(R.drawable.add_user)

// 낮은 버젼 호환을 위해 Compat API사용
ResourcesCompat.getDrawable(getResources(), R.drawable.lock, null),
```

## onPostCreate & onPostResume
`onPostCreate() 와 onPostResume()`

이 두 함수는 시스템 상에서 마지막 초기화 작업을 목적으로 만들어진 것으로 일반적으로 어플리케이션 작성시에는 구현할 필요가 없다고 한다.

## Button Listener
- `setContentView`에 지정한 레이아웃안에 있는것들만 Button 이벤트를 걸 수 있음

## Linear Layout으로 멀티디바이스 지원하기
-  `layout_weight`로 하면됨

양쪽에 공백을 좀 주면서 가운데 정렬을 하고 싶을때

```python
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="horizontal"
            android:weightSum="10"
            >

            <android.support.v4.widget.Space
                android:layout_width="0dp"
                android:layout_height="match_parent"
                android:layout_weight="2"
                />

            <android.support.v7.widget.AppCompatButton
                android:id="@+id/btn_login"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_marginTop="24dp"
                android:layout_marginBottom="24dp"
                android:padding="12dp"
                android:layout_weight="3"
                android:text="Login"/>

            <android.support.v7.widget.AppCompatButton
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_marginTop="24dp"
                android:layout_marginBottom="24dp"
                android:padding="12dp"
                android:layout_weight="3"
                android:text="Signup"
                />

            <android.support.v4.widget.Space
                android:layout_width="0dp"
                android:layout_height="match_parent"
                android:layout_weight="2"
                />
        </LinearLayout>
```

### 안드로이드 Application
- 안드로이드에서 공통된 전역변수(싱글톤)를 사용하고 싶을때 Application을 활용할 수 있다.
- 헌데, 간혹 까먹고 `AndroidManifest.xml`에 집어 넣지 않으면 아래와 같은 에러가 나온다.

```
Caused by: java.lang.ClassCastException: android.app.Application cannot be cast to xxxxxxx
```

위와같이 CastingException이 발생하는데 그럴때면 아래와 같이 `AndroidManifest.xml`에 
`application`에 `name`을 지정해준다.


```
<application
	android:name=".MyApplication"
>
	
</application>
```


**까먹지 말자!!**
