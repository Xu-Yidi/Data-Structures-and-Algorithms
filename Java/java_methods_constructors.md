## Java Methods & Constructors
### Methods(函數/方法)
A Java method is a collection of statements that are grouped together to perform an operation.

#### Defining a Method
In general, a method has the following syntax:
```java
Modifier returnValueType methodName(list of parameters){
    method body;
}
```
- Modifier(修飾符): 
  - Access-Modifier(訪問修飾符): public/private/default
  - Non-Access Modifer(非訪問修飾符): static
- returnValueType(返回值類型): 如果方法不返回任何值，則返回值類型為void; 如果方法具有返回值，則需要制定返回值的類型，並在method body中使用return返回值
- methodName(方法名): 需使用合法的標識符
- list of parameters(參數列表): 傳遞給方法的參數列表，每個參數由參數類型與參數名組成，參數間以逗號隔開

#### Method Overloading(方法重載)
1.A method with the same name as the another method in the same calss is called an **overloaded method**;<br>
2.An overloaded method must differ from other methods of the same name in number or types of parameters;<br>
3.All overloaded method's return type must match to avoid conflict of use.<br>
總結：即方法名稱相同，參數的類型與個數不同，且返回值的類型需相同

#### Recursion(遞迴)
Recursive algorithm involves at least two cases:
- Base Case: A simple occurrence that can be answered directly
- Recursive Case: A more complex occurrence of the problem that cannot be directly answered, but can instead be described in terms of smaller occurrences of the same problem.

#### Examples
```java
public class MethodTest{
    public static void main(String[] args){
        MethodTest mt = new MethodTest();
        mt.show_1();
        
        String content = mt.show_2();
        System.out.println(content);
        
        mt.show_3("Susan");
        
        float BMI = mt.show_4(1.60f, 53);
        System.out.println("Your BMI is " + BMI +"!");
        
        float age = mt.show_4(1997);
        System.out.println("You are " + age + " years old!");
        
        int product = factorial(10);
        System.out.println(product);
    }
    
    
    public void show_1(){                   
        System.out.println("Hello World!");
    }
    public String show_2(){
        return "Java is interesting!";
    }
    public void show_3(String name){
        System.out.println("Welcome to Java programming world" + name + "!");
    }
    public float show_4(float height, int weight){
        return weight%(height*height);
    }
    public float show_4(int birthyear){           //overload
        return 2020-birthyear;
    }
    public static int factorial(int n){          //recursive
        if (n==1) return 1;
        else
            return factorial(n-1)*n;
    }
   
}
```

### Constructors(建構函數/建構方法)
1.A construtor is the code that runs when somebody says **new** on a class type.<br>
2.A constructor must have the **same name** as the class, and **no** return type.<br>
3.If you don't put a constructor in your class, the compiler puts in a **default constructor**. The default constructor is always a no-arg constructor.<br>
4.You can have more than one constructor in your class, as long as the argument lists are different. Having more than one constructor in a class means you have **overload** constructors.<br>

### Methods  V.S. Constructors
1.一般函數用於定義對象應該具備的功能，而構造函數定義對象建立時應該具備的內容，即初始化對象內容;<br>
2.一般函數可以多次調用，構造函數只在創建對象時調用;<br>
3.構造函數的函數名稱需與class名稱一致，一般函數的函數名稱只需符合命名規則即可;<br>
4.構造函數不需返回值類型.<br>

### Example

```java
public class TestDuck {
	public static void main(String[] args) {
		int weight = 8;
		String name = "Donald";
		boolean canFly = true;

		Duck[] d = new Duck[3];
		d[0] = new Duck();
		d[1] = new Duck(canFly);
		d[2] = new Duck(name, weight);
		System.out.println(d[0].sound());
	}
}

class Duck{
	int pounds;
	String name;
	boolean canFly;

	public Duck() {                       //constructor
		System.out.println("type 1 duck");
	}
	public Duck(boolean fly) {            //overload
		canFly = fly;
		System.out.println("type 2 duck");
	}
	public Duck(String n, int w) {        //overload
		name = n;
		pounds = w;
		System.out.println("type 3 duck");
	}
	public String sound() {                //method
		return "quack";		
	}
}
```
Reference:<br>
https://blog.csdn.net/qq_33642117/article/details/51909346<br>
https://blog.csdn.net/HoHiuChing/article/details/77480471<br>
https://blog.csdn.net/mrbacker/article/details/79181869
