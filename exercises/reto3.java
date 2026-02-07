import java.util.HashMap;
import java.util.Map;

public class StringChallenge {
    
    public static String stringChallenge(String str) {
        // Crear el diccionario de mapeo
        Map<Character, Character> dic = new HashMap<>();
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        
        for (int i = 0; i < alphabet.length(); i++) {
            char current = alphabet.charAt(i);
            char next = alphabet.charAt((i + 1) % alphabet.length());
            dic.put(current, next);
        }
        
        StringBuilder resultado = new StringBuilder();
        String token = "hbs2oim9c1a";
        String vocales = "aeiou";
        
        // Transformar la cadena
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            char lower = Character.toLowerCase(c);
            
            if (dic.containsKey(lower)) {
                char nuevo = dic.get(lower);
                if (vocales.indexOf(nuevo) != -1) {
                    resultado.append(Character.toUpperCase(nuevo));
                } else {
                    resultado.append(nuevo);
                }
            } else {
                resultado.append(c);
            }
        }
        
        String cadena = resultado.toString();
        
        // Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every fourth character with an underscore.
        StringBuilder finalResult = new StringBuilder();
        String combined = cadena + token;
        for (int i = 0; i < combined.length(); i++) {
            if ((i + 1) % 4 == 0) {
                finalResult.append('_');
            } else {
                finalResult.append(combined.charAt(i));
            }
        }
        
        return finalResult.toString();
    }
    
    public static void main(String[] args) {
        String r1 = stringChallenge("hello*3");
        String r2 = stringChallenge("fun times!");
        System.out.println(r1);
        System.out.println(r2);
    }
}