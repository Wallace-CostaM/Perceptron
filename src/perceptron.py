import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=1000):
        # Inicializa pesos com zero, incluindo o bias (entrada fixa 1)
        self.weights = np.zeros(input_size + 1)  # +1 para o bias
        self.lr = learning_rate
        self.epochs = epochs

    def activation_fn(self, x):
        # Step Function: retorna 1 se x >= 0, senão 0
        return 1 if x >= 0 else 0

    def predict(self, x):
        # Adiciona bias à entrada (x0 = 1)
        x = np.insert(x, 0, 1)  # adiciona bias = 1 na frente
        z = np.dot(x, self.weights)
        return self.activation_fn(z)

    def train(self, X, y):
        # Treinamento com atualização dos pesos baseado no erro
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi_bias = np.insert(xi, 0, 1)  # bias
                z = np.dot(xi_bias, self.weights)
                y_pred = self.activation_fn(z)
                error = target - y_pred
                self.weights += self.lr * error * xi_bias

    def evaluate(self, X):
        return [self.predict(xi) for xi in X]

# OR é linearmente separável, logo o perceptron pode aprender essa função.
if __name__ == "__main__":
    # Dataset para função lógica OR (pode ser trocado por AND, XOR, etc)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 1, 1, 1])
    # Exemplo de y para OR: [0, 1, 1, 1]
    # Se usarmos y = [0, 1, 1, 0] (XOR), o perceptron não conseguirá aprender, pois XOR não é linearmente separável.

    # X são as entradas (pares binários)
    # y são as saídas esperadas


    p = Perceptron(input_size=2)
    p.train(X, y)

    print("Pesos finais (bias, w1, w2):", p.weights)

    for i, xi in enumerate(X):
        pred = p.predict(xi)
        print(f"Entrada: {xi}, Predição: {p.predict(xi)}, Real: {y[i]}")