# Projeto Perceptron Simples

## 1. Introdução
O perceptron é um modelo básico de rede neural de camada única, utilizado como classificador linear binário. Ele é aplicado em problemas de aprendizado supervisionado, classificando dados de entrada em duas categorias distintas.

O projeto foi elaborado para testar conhecimentos de forma prática e explorar de forma profunda os conceitos existentes na construção e implementação do perceptron, e todo o ecossistema que envolve essa arquitetura.

Atualmente, este trabalho faz parte de um estudo voltado para a área de Data Science. O projeto funciona como um manual didático do funcionamento do perceptron e da estrutura básica das redes neurais.

## 2. Conceitos básicos
O perceptron consiste em 4 partes:
1. Valores de entrada
2. Pesos e Viés
3. Soma Ponderada
4. Função de Ativação

O perceptron trabalha da seguinte maneira:
a. todas as entradas Xi são multiplicadas por seus respectivos pesos Wi, dando corpo a uma fórmula: X1 . W1 + X2 . W2 + ... + Xn . Wn = K. Esta soma pode ser vista como um produto escalar entre os vetores de entrada e pesos.
b. Adiciona-se o viés, que é um peso fixo aplicado a uma entrada constante (geralmente 1). O viés permite deslocar a fronteira de decisão, ajustando o limiar para ativação do neurônio. O resultado da soma ponderada mais o viés para a função de ativação, que decide se o neurônio "dispara" ou não. No perceptron simples, a função de ativação usada é a Step Function, que retorna 1 se o valor for maior ou igual a zero, e 0 caso contrário.

Precisamos dos pesos para mostrar a força de um nó em específico. E o viés permite você deslocar a curva da função de ativação para cima ou para baixo. A função de ativação é usada como mapa para a entrada que requer valores entre 0 e 1, ou -1, 1.

O perceptron é um classificador binário linear, capaz de separar os dados em duas classes por meio de uma linha (ou hiperplano) de decisão.

Um exemplo clássico é a função lógica OR, onde as entradas A e B produzem uma saída 0 somente se ambas forem 0; caso contrário, a saída é 1. O perceptron treinado para aprender a função OR se comporta de forma semelhante à operação lógica de disjunção.

## 3. Dataset utilizado
Neste projeto, utilizamos um conjunto de dados simples para demonstrar o funcionamento do perceptron. As entradas são pares binários representando todas as combinações possíveis de dois bits. Este conjunto corresponde à função lógica OR, onde a saída é 1 sempre que pelo menos uma das entradas é 1, e 0 caso contrário. Esse conjunto de dados é pequeno e simples, mas suficiente para exemplificar como o perceptron aprende a classificar dados linearmente separáveis.

## 4. Limitações do perceptron simples
O perceptron simples possui uma única camada de entrada e uma única unidade de saída, o que limita sua capacidade em resolver problemas que não são linearmente separáveis, como o problema do XOR (Exclusive OR).

No caso do XOR, para duas entradas X1 e X2, a saída é 1 somente quando exatamente uma das entradas for 1. Ou seja:
- X1 = 0, X2 = 1 -> saída 1
- X1 = 1, X2 = 0 -> saída 1
- X1 = 0, X2 = 0 -> saída 0
- X1 = 1, X2 = 1 -> saída 0

Esse padrão não pode ser separado por uma única linha (hiperplano) no espaço das entradas, impossibilitando para o perceptron simples aprender corretamente essa função. Portanto, o perceptron simples falha ao tentar aprender o XOR.

## 5. Como usar o código
Requisitos:
- python 3.x instalado no seu computador
- bibliotecas necessárias: numpy, matplotlib
  - Você pode instalar as bibliotecas usando: pip install numpy matplotlib

Como Rodar:
- Clone este repositório ou baixe os arquivos do projeto.
- Navegue até a pasta do projeto no terminal ou prompt de comando.
- Execute o script principal, por exemplo: python perceptron.py
- O programa vai treinar o perceptron com o dataset de exemplo e mostrar os pesos finais, além de imprimir as predições para as entradas testadas.

## 6. Resultados esperados
Ao executar o código com o conjunto de dados da função lógica OR, você deverá observar:
- Os pesos finais do perceptron após o treinamento, que indicam a importância de cada entrada e do viés para a decisão.
- As predições para cada combinação de entrada, impressas no terminal.
- O perceptron deverá classificar corretamente todas as entradas, mostrando que aprendeu a função OR.
- Caso use um dataset não linearmente separável, como XOR, o perceptron não conseguirá classificar corretamente todas as entradas, e os erros persistirão após o treinamento.

## 7. Possíveis melhorias
- Implementar perceptron multicamadas (MLP) para resolver problemas não linearmente separáveis, como XOR.
- Adicionar outras funções de ativação, como sigmoid, ReLU ou tanh.
- Adaptar o perceptron para classificação multiclasse.
- Testar o modelo com datasets reais, como o conjunto Iris.
- Implementar testes automatizados para garantir a robustez do código.



## 8. Referências
