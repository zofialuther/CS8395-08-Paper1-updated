```python
import os

os.system("echo public class X { public static void main(String[] args) { System.out.println(\"Hello Java!\"); } } > X.java")
os.system("javac X.java")
os.system("java X")
```