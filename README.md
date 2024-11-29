### **README - Interpretador Turtle com ANTLR**

---

### **Descrição do Projeto**

Este projeto implementa um interpretador gráfico utilizando a biblioteca **Turtle** do Python e o **ANTLR** para processar uma linguagem personalizada chamada **Desenhar**. A linguagem permite criar desenhos geométricos baseados em comandos simples, como mover, girar, alterar a cor e repetir blocos de comandos.

Um exemplo incluído no projeto desenha a palavra **"compilar"** ao ser executado, ilustrando as capacidades da linguagem.

---

### **Requisitos**

1. **Python 3.7+**
2. **ANTLR 4**
3. **Pacotes Python necessários:**
   - `antlr4-python3-runtime`
   - `turtle` (parte do Python por padrão)

---

### **Instalação**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale o runtime do ANTLR para Python:
   ```bash
   pip install antlr4-python3-runtime
   ```

3. Gere os arquivos de análise léxica, sintática e o visitante com o seguinte comando:
   ```bash
   antlr4 -Dlanguage=Python3 -visitor Desenhar.g4
   ```

4. Certifique-se de que os seguintes arquivos foram gerados:
   - `DesenharLexer.py`
   - `DesenharParser.py`
   - `DesenharVisitor.py`

---

### **Como Usar**

1. **Criar um Arquivo de Entrada:**
   Crie um arquivo `.txt` contendo os comandos da linguagem **Desenhar**. Por exemplo:
   ```txt
   COLOR RED;
   PENDOWN;
   REPEAT 4 {
       MOVE 100;
       TURN 90;
   }
   PENUP;
   MOVE 200;
   ```

2. **Executar o Interpretador:**
   Use o terminal para executar o interpretador com o arquivo de entrada como argumento:
   ```bash
   python interpretador.py <nome-do-arquivo>
   ```

3. Uma janela gráfica será aberta exibindo o desenho gerado.

---

### **Comandos da Linguagem Desenhar**

| Comando           | Descrição                                              | Exemplo                 |
|--------------------|--------------------------------------------------------|-------------------------|
| `MOVE <N>;`       | Move a tartaruga para frente por `<N>` unidades.        | `MOVE 100;`            |
| `TURN <N>;`       | Gira a tartaruga `<N>` graus para a direita.            | `TURN 90;`             |
| `PENDOWN;`        | Abaixa a caneta para começar a desenhar.                | `PENDOWN;`             |
| `PENUP;`          | Levanta a caneta para parar de desenhar.                | `PENUP;`               |
| `COLOR <COR>;`    | Muda a cor da caneta.                                   | `COLOR RED;`           |
| `REPEAT <N> { ... }` | Repete um bloco de comandos `<N>` vezes.             | `REPEAT 4 { MOVE 50; TURN 90; }` |

**Cores disponíveis:** `RED`, `GREEN`, `BLUE`, `BLACK`, `YELLOW`.

---

### **Exemplo Completo**

Arquivo `entrada.txt`:
```txt
COLOR BLUE;
PENDOWN;
MOVE 150;
TURN 90;
COLOR GREEN;
MOVE 100;
TURN 90;
REPEAT 4 {
    COLOR YELLOW;
    MOVE 50;
    TURN 45;
}
PENUP;
MOVE 200;
```

Comando:
```bash
python interpretador.py entrada.txt
```

Saída: Um desenho será gerado seguindo as instruções do arquivo.

---

### **Desenho de "compilar"**

Um exemplo incluído no projeto desenha a palavra **"compilar"**. Para testá-lo:

1. Localize o arquivo de entrada de exemplo no diretório `examples/compilar.txt`.

2. Execute o interpretador com o comando:
   ```bash
   python interpretador.py examples/compilar.txt
   ```

3. Uma janela será aberta desenhando a palavra **"compilar"**.

---
