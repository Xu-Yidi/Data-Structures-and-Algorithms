## Java Array(陣列/數組)
An array is a data structure used to process a collection of data that is all of the **same type**.<br>
Arrays are always **objects**, whether they're declared to hold primitive(原始型別)or object reference(引用型別).

### Declaration/Initialization of an Array(初始化)
- Dynamic Initialization(動態初始化): 動態初始化是指在定義時先指定數組長度，由系統先自動為其賦值
```java
type[] name = new type[size];
```
EX.
```java
public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[3];
        
        for(int a:array){
        System.out.print(a + " ");
        }
    }
}
//result: 0 0 0
```
- Static Intialization(靜態初始化): 靜態初始化是指在定義時指定數組元素的內容，並由系統決定其長度
```java
type[] name = new type[] {elements};
```
EX.
```Java
public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {1,2,3};
        
        for(int a:array){
        System.out.print(a + " ");
        }
    }
}
//result: 1 2 3
```
### Some Useful Methods
- array.length
```java
public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {1,2,3};
        System.out.print(array.length);
    }
}
//result: 3
```
#### java.util.Arrays中的常用方法
- Arrays.fill(object[] array, int fromIndex, int ToIndex, object obj); 從指定的起始位置至結束位置使用指定元素填充數組

```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {1,2,3,4,5};
        
        Arrays.fill(array, 10);
        for (int a:array){
            System.out.print(a + " ");
        }
        
        System.out.println();
        
        Arrays.fill(array, 1, 4, 6);  //取起始位置不取結束位置
        for (int a:array){
            System.out.print(a + " ");
        }        
    }
}
//result: 10 10 10 10 10
//        10 6 6 6 10
```
- Array.sort(object[] array, int fromIndex, int toIndex); 對指定位置範圍內的元素進行排序
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {5,4,3,2,1};
        
        Arrays.sort(array);
        for (int a:array){
            System.out.print(a + " ");
        }
    }
}
//result: 1 2 3 4 5
```
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {5,4,3,2,1};
        
        Arrays.sort(array, 1, 4);
        for (int a:array){
            System.out.print(a + " ");
        }
    }
}
//result: 5 2 3 4 1
```
- Arrays.binarySearch(object[], int fromIndex, int toIndex, obj key); 使用二分搜尋法查找數組指定範圍內指定元素的索引值<br>Hint:<br>1.在使用二分搜尋法前，應先調用Arrays.sort()對數組進行排序，如果數組尚未排序，則結果並不確定，且若數組中包含多個指定元素，則無法保證找到其中哪個元素;<br> 2.當數組包含搜尋元素時，返回該元素的索引值，若數組不包含指定元素，則將指定元素視為存在於數組中，並返回-(索引值+1)

```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {9,7,5,3,1};
        Arrays.sort(array);
        System.out.println(Arrays.binarySearch(array, 3)); // 1
        System.out.println(Arrays.binarySearch(array, 0)); //-1 將數組視為{0,1,3,5,7,9}，index為-(0+1)=-1
        System.out.println(Arrays.binarySearch(array, 11)); //-6 將數組視為{1,3,5,6,9,11}，index為-(5+1)=-6
        System.out.println(Arrays.binarySearch(array, 4)); //-3 將數組視為{1,3,4,5,6,9}，index為-(2+1)=-3
        System.out.println(Arrays.binarySearch(array, 1, 3, 3)); 
    }
}
```
- Array.copyOf(object[] original, int newLength); 複製數組，從下標位置為0開始，超過原先數組長度則用null填滿
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {9,7,5,3,1};
        int[] array_1 = Arrays.copyOf(array, 7);
        
        for (int a:array_1){
            System.out.print(a + " ");
        }
    }
}
//result: 9 7 5 3 1 0 0 
```
- Arrays.copyOfRange(object[] original, int fromIndex, int toIndex); 指定起始位置與結束位置複製數組，若超過原先數組長度，則使用null填充
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {9,7,5,3,1};
        int[] array_1 = Arrays.copyOfRange(array, 1, 3); //取起始位置不取結束位置
        
        for (int a:array_1){
            System.out.print(a + " ");
        }
    }
}
//result: 7 5
```
- Arrays.equals(object[] array1, object[] array2); 判斷兩個數組元素是否相等
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {9,7,5,3,1};
        int[] array_1 = new int[] {9,7,5,3,1};
        System.out.println(Arrays.equals(array, array_1));
    }
}
//result: true
```
- Arrays.hashCode(object[] array); 返回數組的哈希值
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {9,7,5,3,1};
        System.out.println(Arrays.hashCode(array));
    }
}
//result: 37154276
```
- Arrays.toString(object[] array);返回數組的字符串形式
```java
import java.util.Arrays;

public class ArrayTest{
    public static void main(String[] args){
        int[] array = new int[] {9,7,5,3,1};
        System.out.println(Arrays.hashCode(array));
    }
}
//result: [9,7,5,3,1]
```

Reference:<br>
[Arrays類常用方法解析](https://blog.csdn.net/Goodbye_Youth/article/details/81003817)<br>







