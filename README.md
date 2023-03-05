# ChatGPT Translator
:star: Translate your text using **ChatGPT**!

This translator uses ChatGPT to translate your text. ChatGPT can understand slang in all languages.
This API uses official OpenAI API. You need to create own API key to use it.

# Example of usage
I made a few examples in different programming languages.

Python:
```python
import chatgpt_translator as Translator # Copy 'chatgpt_translator.py' from this repository inside your project

print(Translator.Translate(source_text = "Hello, how are you?", awaited_lang = "Russian", token = "sk-...")) # Привет, как дела?
```

Java:
```java
import org.json.JSONObject;

public static void main(String[] args) throws IOException {
        String api = "https://chatgpttranslator.netrumnetrum.repl.co/translate";
        URLConnection connection = new URL(String.format("%s?text=%s&awaited_lang=%s&token=%s",
                api, // API Host
                "Hello, how are you?".replace(" ", "%20"), // Input text
                "Russian", // Awaited language
                "sk-..." // OpenAI token
        )).openConnection();


        // Read the response
        String response = new BufferedReader(new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8)).readLine();

        JSONObject json = new JSONObject(response);
        String rawText = json.getString("translated_text"); // This API returns JSON-style response. We need to parse it.

        System.out.printf("%s\n", rawText); // Привет, как дела?
    }
```
