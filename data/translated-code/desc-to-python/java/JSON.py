import com.google.gson.Gson;

public class Main {
    public static void main(String[] args) {
        Gson gson = new Gson();
        
        // Parsing JSON to Java object
        String json = "{\"foo\":123, \"bar\":[\"hello\", \"world\"]}";
        MyJsonObject myObject = gson.fromJson(json, MyJsonObject.class);
        System.out.println("foo: " + myObject.getFoo());
        System.out.println("bar: " + Arrays.toString(myObject.getBar()));
        
        // Converting Java object to JSON
        MyJsonObject newObj = new MyJsonObject(456, new String[]{"goodbye", "world"});
        String newJson = gson.toJson(newObj);
        System.out.println(newJson);
    }
}

class MyJsonObject {
    private int foo;
    private String[] bar;
    
    public MyJsonObject(int foo, String[] bar) {
        this.foo = foo;
        this.bar = bar;
    }
    
    public int getFoo() {
        return foo;
    }
    
    public String[] getBar() {
        return bar;
    }
}