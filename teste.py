import matplotlib.pyplot as plt

# Função dos graficos!
def matplotlib_plot():
    x = np.linspace(-10, 10, 100)
    y = x**2
    plt.plot(x, y)
    plt.title("Function y = x^2")
    plt.show()