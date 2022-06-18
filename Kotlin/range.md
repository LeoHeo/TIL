> Kotlin lets you easily create ranges of values using the rangeTo() function from the kotlin.ranges package and its operator form ... Usually, rangeTo() is complemented by in or !in functions.

Kotlin에 있는 rangeTo (in, !in)을 사용하면 쉽게 range을 구할 수 있음


```java
LocalDateTime fromTime = LocalDateTime.parse("2022-06-18 12:00:33", java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
LocalDateTime toTime = LocalDateTime.parse("2022-06-18 12:30:33", java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
LocalDateTime targetTime = LocalDateTime.parse("2022-06-18 12:20:33", java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));

if ((targetTime.equals(toTime) || targetTime.equals(fromTime))
        || (targetTime.isAfter(fromTime) && targetTime.isBefore(toTime))) {
    System.out.println("java date time range");
}
```


```kotlin
val fromTime = LocalDateTime.parse("2022-06-18 12:00:33", DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
val toTime = LocalDateTime.parse("2022-06-18 12:30:33", DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
val targetTime = LocalDateTime.parse("2022-06-18 12:20:33", DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))

if (targetTime in fromTime..toTime) {
    println("kotlin date time range")
}
```


## Enum range

```java
public enum Status {
    TEST,
    TEST2,
    NO;
    
    public boolean isTest() {
        return Arrays.asList(TEST, TEST2).contains(this);
    }
}

// 실제로 쓸때
System.out.println(Status.NO.isTest());
System.out.println(Status.TEST.isTest());
```

```kotlin
enum class Status {
    TEST,
    TEST2,
    NO;

    fun isTest(): Boolean {
        return this in listOf(TEST, TEST2)
    }
}

// 실제로 쓸때
println(Status.NO.isTest())
println(Status.TEST2.isTest())
```