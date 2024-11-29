### **README - Interpretador Turtle com ANTLR**

---

### **Equipe**
- **Gabriel Agra**  
- **Gabriel Alves**

---

### **Motivação**

O projeto foi desenvolvido com o objetivo de explorar conceitos de linguagens de programação e compiladores. A linguagem **Desenhar** foi criada para ser simples e intuitiva, permitindo que usuários criem desenhos geométricos ou textos na tela utilizando comandos estruturados.  

Além disso, este projeto demonstra a integração entre ferramentas como **ANTLR**, para criação de gramáticas e análise sintática, e a biblioteca gráfica **Turtle**, que fornece uma maneira divertida e visual de interpretar os comandos.

---

### **Descrição da Linguagem Desenhar**

A linguagem **Desenhar** foi projetada para ser minimalista e funcional. Com ela, é possível mover uma "tartaruga gráfica" na tela, mudar sua direção, alterar a cor do traço, levantar ou abaixar a caneta para desenhar ou não, e repetir comandos em blocos.

**Principais recursos da linguagem:**
1. **Movimento**: Controle do deslocamento da tartaruga.
2. **Direção**: Controle do ângulo de rotação.
3. **Cores**: Alteração da cor da caneta.
4. **Repetição**: Execução de blocos de comandos múltiplas vezes.

**Exemplo de programa simples:**
```txt
COLOR RED;
PENDOWN;
REPEAT 4 {
    MOVE 100;
    TURN 90;
}
PENUP;
```

Neste exemplo, a tartaruga desenha um quadrado vermelho.

---

### **Guia de Execução**

#### **Requisitos**
1. **Python 3.7+** instalado no sistema.
2. **ANTLR 4** instalado (para gerar os analisadores léxicos e sintáticos).
3. Pacote Python:
   ```bash
   pip install antlr4-python3-runtime
   ```

#### **Passos para execução**

1. **Clonar o projeto:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Gerar arquivos do ANTLR:**
   Execute o comando abaixo para gerar os arquivos do analisador léxico, sintático e visitante:
   ```bash
   antlr4 -Dlanguage=Python3 -visitor Desenhar.g4
   ```

3. **Criar um arquivo de entrada:**
   Crie um arquivo `.txt` contendo o código da linguagem **Desenhar**.

   Exemplo (`entrada.txt`):
   ```txt
   COLOR BLUE;
   PENDOWN;
   MOVE 100;
   TURN 90;
   REPEAT 4 {
       COLOR GREEN;
       MOVE 50;
       TURN 45;
   }
   PENUP;
   ```

4. **Executar o interpretador:**
   Use o seguinte comando para interpretar o programa:
   ```bash
   python interpretador.py entrada.txt
   ```

---

### **Exemplos de Programas**

#### **Exemplo 1: Quadrado Vermelho**
```txt
COLOR RED;
PENDOWN;
REPEAT 4 {
    MOVE 100;
    TURN 90;
}
PENUP;
```

Saída: Um quadrado vermelho será desenhado.

#### **Exemplo 2: Desenho de "compilar"**
Arquivo `compilar.txt`:
```txt
COLOR BLACK;
PENDOWN;
MOVE 50;
TURN 90;
MOVE 100;
PENUP;
TURN 90;
MOVE 50;
...
```

Comando:
```bash
python interpretador.py compilar.txt
```

Saída: O desenho da palavra **"compilar"** aparecerá na janela gráfica.

---
