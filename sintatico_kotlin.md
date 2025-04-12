
# 📗 Documentação Sintática da Linguagem Kotlin

## 1. Elementos Sintáticos

Um programa em Kotlin é composto por uma ou mais funções, podendo estar dentro ou fora de classes. A estrutura básica de uma função Kotlin pode ser expressa pela seguinte regra:

```
funcao → "fun" ID "(" Params ")" ":" tipo "{" statements "}"
```

Onde:
- `fun` é a palavra-chave que inicia a função.
- O primeiro `ID` é o nome da função.
- `params` representa os argumentos da função (lista de parâmetros).
- `type` indica o tipo de retorno.
- `statements` representa um ou mais comandos dentro do corpo da função.

A seguir, veremos os comandos permitidos em Kotlin.

---

## 1.1 Comandos da Linguagem Kotlin

Kotlin permite comandos de expressão, comandos de controle como `if`, `when`, `while`, e `return`, conforme regras abaixo:

```
statements → exp
      | WHILE "(" exp ")" "{" stms "}"
      | RETURN exp
      | IF "(" exp ")" stm (ELSE stm)?
      | WHEN "(" exp ")" "{" branches "}"
```

- O comando `while` inicia com a palavra-chave `while`, seguido de uma expressão entre parênteses e um bloco de comandos entre chaves.
- O comando `return` retorna uma expressão e encerra a função.
- O comando `if` avalia uma expressão condicional e executa comandos de acordo com o resultado.

---

## 1.2 Expressões em Kotlin

Kotlin suporta expressões aritméticas, chamadas de função, atribuições, e expressões lógicas. Sua gramática pode ser descrita por:

```
exp → exp "+" exp
     | exp "-" exp
     | exp "*" exp
     | exp "/" exp
     | call
     | assign
     | NUM
     | STRING
     | BOOLEAN
     | ID
```

---

### 1.2.1 Chamadas de Função e Atribuição

Chamadas de função e atribuições em Kotlin seguem as seguintes regras:

```
call → ID "(" params ")"
params → exp "," params | exp | ε
assign → ID "=" exp
```

Kotlin permite chamadas com ou sem parâmetros, e permite atribuição de variáveis com `=`.

---

## 2. Exemplos de Código

```kotlin
fun soma(a: Int, b: Int): Int {
    return a + b
}

fun exemploLoop() {
    var i = 0
    while (i < 5) {
        println(i)
        i++
    }
}

fun condicional(x: Int) {
    if (x > 10) {
        println("Maior que 10")
    } else {
        println("10 ou menos")
    }
}

```

