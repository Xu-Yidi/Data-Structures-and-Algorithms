## Java Modifiers
Java的修飾符根據修飾對象不同，分為類修飾符(class modifier)，方法修飾符(method modifier)以及變量修飾符(variable modifier)，其中每種修飾符又分為訪問控制修飾符(access modifier)和非訪問控制修飾符(non-access modifier).

### Class Modifires(類修飾符)
#### Access Modifiers: public/default
- public class
  - 如果使用public class聲明某個類，則該類名稱需與文件名稱相同
  - 被public修飾的類可被其他package訪問
  - 在一個.java文件中，只能存有一個public class
- (default)class
  - 如果只使用class聲明某個類，該類名稱可與文件名稱不一致
  - 若無public修飾，則該類只能用於該package中
  - 在一個.java文件，能存在多個class
#### Non-Access Modifiers: abstract/final
此為更進階之內容，暫不說明

### Method Modifiers(方法修飾符)
#### Access Modifiers: public/default/private/protected
protected為更進階之內容，暫不說明，且訪問為通過對象實例訪問

- public method
  - 可以在聲明的同一個class訪問
  - 可以在同一個package中的不同class訪問
  - 可以在不同package中訪問
```java
public class MethodTest{
    public static void main(String[] args){
    MethodTest mt = new MethodTest();
    mt.show();
    }
    public void show(){
        System.out.println("Hello World!");
    }
}
//result: Hello World!
```
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest pt = new PrintTest();
    pt.show();
    }
}
class PrintTest{
    public void show(){
        System.out.println("Hello World!");
    }
}
//result: Hello World!
```
- default
  - 可以在聲明的同一個class中訪問
  - 可以在同一個package中的不同class訪問
  - 無法在不同的package中訪問
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest pt = new PrintTest();
    pt.show();
    }
}
class PrintTest{
    void show(){
        System.out.println("Hello World!");
    }
}
//result: Hello World!
```
- private
  - 可以在聲明的同一個class中訪問
  - 無法在同一個package中的不同class訪問
  - 無法在不同的package中訪問
```java
public class MethodTest{
    public static void main(String[] args){
    MethodTest mt = new MethodTest();
    mt.show();
    }
    
    private void show(){
        System.out.println("Hello World!");
    }
}
//result: Hello World!
```
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest pt = new PrintTest();
    pt.show();
    }
}
class PrintTest{
    private void show(){
        System.out.println("Hello World!");
    }
}
//result:/MethodTest.java:4: error: show() has private access in PrintTest
```
#### Non-Access Modifiers: abstract/static/final/native/synchronized
此處暫時只討論static(靜態方法修飾符)，其餘為更進階之內容，暫不說明

- static 
  - 可以直接通過類名訪問，而無需先實例化類，也可以實例化後訪問
  - 只能訪問所屬類的靜態變量與靜態方法

```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest.show();
    }
}
class PrintTest{
    public static void show(){
        System.out.println("Hello World!");
    }
}
//result: Hello World!
```
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest.show();
    }
}
class PrintTest{
    static String content = "Hello World!";
    public static void show(){
        System.out.println(content);
    }
}
//result: Hello World!
```
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest.show();
    }
}
class PrintTest{
    String content = "Hello World!";
    public static void show(){
        System.out.println(content);
    }
}
//result: /MethodTest.java:9: error: non-static variable content cannot be referenced from a static context
```
- non-static
  - 只可以實例化類後訪問
  - 可以訪問所屬類的靜態/非靜態變量以及靜態/非靜態方法



```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest pt = new PrintTest();
    pt.show();
    }
}
class PrintTest{
    static String content = "Hello World!";
    public void show(){
        System.out.println(content);
    }
}
//result: Hello World!
```
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest.show();
    }
}
class PrintTest{
    public void show(){
        System.out.println("Hello World!");
    }
}
//result: /MethodTest.java:3: error: non-static method show() cannot be referenced from a static context
```
### Variable Modifiers
#### Access Modifiers: public/default/private/protected
與Method部分相似
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest pt = new PrintTest();
    System.out.println(pt.content);
    }
}
class PrintTest{
    public String content = "Hello World!";
}
//result: Hello World!
```
```java
public class MethodTest{
    public static void main(String[] args){
    PrintTest pt = new PrintTest();
    System.out.println(pt.content);
    }
}
class PrintTest{
    private String content = "Hello World!";
}
//result: /MethodTest.java:4: error: content has private access in PrintTest
```
#### Non-Access Modifiers: static/final/volatile/transient
與Method部分相似<br>
```java
public class MethodTest{
    public static void main(String[] args){
    System.out.println(PrintTest.content);
    }
}
class PrintTest{
    static String content = "Hello World!";
}
//result: Hello World!
```
Reference:<br>
[Java中類的public class與class的區別詳解](https://blog.csdn.net/jingzi123456789/article/details/71515728)<br>
[Java修飾符的總結](https://blog.csdn.net/u012723673/article/details/80613557)<br>
[我的理解之Java權限的4種訪問](https://blog.csdn.net/u010876691/article/details/72724415)<br>
[Java中static 作用及用法詳解](https://blog.csdn.net/fengyuzhengfan/article/details/38082999)
