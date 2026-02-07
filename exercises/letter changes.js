function StringChallenge(str) {
  let abc = new Map();
    abc.set("a", "b");
    abc.set("b", "c")
    abc.set("c", "d")
    abc.set("d", "e")
    abc.set("e", "f")
    abc.set("f", "g")
    abc.set("g", "h")
    abc.set("h", "i")
    abc.set("i", "j")
    abc.set("j", "k")
    abc.set("k", "l")
    abc.set("l", "m")
    abc.set("m", "n")
    abc.set("n", "o")
    abc.set("o", "p")
    abc.set("p", "q")
    abc.set("q", "r")
    abc.set("r", "s")
    abc.set("s", "t")
    abc.set("t", "u")
    abc.set("u", "v")
    abc.set("v", "w")
    abc.set("w", "x")
    abc.set("x", "y")
    abc.set("y", "z")
    abc.set("z", "a")

    let cadena = [];
    let vocales = "aeiou";
    let token = "6p2m4i8s1bd";

    for (var i = 0; i < str.length; i++){
        if (abc.has(str[i])){
          if (vocales.includes(abc.get(str[i])) === true) {
            cadena.push(abc.get(str[i]).toUpperCase());
          } else {
            cadena.push(abc.get(str[i]))
          }
          
        }
        else{
          cadena.push(str[i])
        }
      }

    let result = cadena.join("");
    let combined = result + token;
    let finalOut = "";

    for(var i = 0; i < combined.length; i++){
      if( (i + 1) % 4 == 0 ){
        finalOut += "_";
      } else {
        finalOut += combined.charAt(i)
      }
    }
        
  return finalOut;
}

// keep this function call here 
console.log(StringChallenge("fun times!"));

