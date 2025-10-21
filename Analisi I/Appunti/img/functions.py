import numpy as np
import matplotlib.pyplot as plt
import cmath

# Configurazione generale dei plot
plt.style.use('default')

# 1. Funzioni Iperboliche (Lezione 12)
def plot_funzioni_iperboliche():
    x = np.linspace(-3, 3, 400)
    sinh_x = np.sinh(x)
    cosh_x = np.cosh(x)

    # Nota: ax è un array di due oggetti Axes: ax e ax[2]
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle('Funzioni Iperboliche (Lezione 12)')

    # --- Primo Subplot: Seno Iperbolico (ax) ---
    ax.plot(x, sinh_x, label='sinh(x)', color='red')
    ax.plot(x, (np.exp(x) - np.exp(-x)) / 2, '--', color='blue', alpha=0.5, label='(e^x - e^{-x}) / 2')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title('Seno Iperbolico (sinh x)')
    ax.set_ylim(-10, 10)
    ax.legend()

    # --- Secondo Subplot: Coseno Iperbolico (ax[2]) ---
    ax[2].plot(x, cosh_x, label='cosh(x)', color='red')
    ax[2].plot(x, (np.exp(x) + np.exp(-x)) / 2, '--', color='blue', alpha=0.5, label='(e^x + e^{-x}) / 2')
    ax[2].axhline(0, color='black', linewidth=0.5)
    ax[2].axvline(0, color='black', linewidth=0.5)
    ax[2].set_title('Coseno Iperbolico (cosh x)')
    ax[2].set_ylim(0, 10)
    ax[2].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# 2. Trasformazione: Valore Assoluto (Lezione 12/Cap. 3)
def plot_valore_assoluto():
    x = np.linspace(-5, 5, 400)
    y = np.abs(x)

    plt.figure(figsize=(6, 5))
    plt.plot(x, y, label='f(x) = |x|', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Funzione Valore Assoluto |x|')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# 3. Funzione Potenza (n pari e n dispari) (Cap. 3, cf.)
def plot_potenze():
    x = np.linspace(-2, 2, 400)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle('Funzioni Potenza $f(x) = x^n$')

    # n Dispari (es. n=3)
    ax.plot(x, x**3, label='$x^3$', color='darkgreen')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title('Potenza Dispari (n=3)')
    ax.legend()
    ax.set_ylim(-8, 8)
    ax.set_xlim(-2, 2)

    # n Pari (es. n=4)
    ax[2].plot(x, x**4, label='$x^4$', color='darkred')
    ax[2].axhline(0, color='black', linewidth=0.5)
    ax[2].axvline(0, color='black', linewidth=0.5)
    ax[2].set_title('Potenza Pari (n=4)')
    ax[2].legend()
    ax[2].set_ylim(0, 8)
    ax[2].set_xlim(-2, 2)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# 4. Piano di Gauss e Modulo (Lezione 13)
def plot_piano_gauss():
    z = complex(3, 4)
    rho = abs(z)

    # Se usiamo plt.figure senza subplot, ax non è un array
    fig, ax = plt.subplots(figsize=(6, 6))

    # Assi cartesiani
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)

    # Punto z
    ax.plot(z.real, z.imag, 'ro', label=f'z = {z.real} + {z.imag}i')

    # Vettore e Modulo
    ax.plot([0, z.real], [0, z.imag], 'b--', label=f'Modulo |z| = {rho:.2f}')

    # Triangolo rettangolo per la forma trigonometrica
    ax.plot([z.real, z.real], [0, z.imag], 'k:', alpha=0.6)
    ax.plot([0, z.real], [z.imag, z.imag], 'k:', alpha=0.6)

    ax.set_xlabel('Reale (a)')
    ax.set_ylabel('Immaginario (b)')
    ax.set_title('Piano di Gauss (Forma Trigonometrica)')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()
    plt.show()

# 5. Successione Decrescente (Esempio 1/n) (Lezione 15)
def plot_successione_decrescente():
    n = np.arange(1, 15)
    a_n = 1 / n

    fig, ax = plt.subplots(figsize=(8, 5))

    # Grafico della successione: 'bo' indica punti blu, '--' linea tratteggiata
    ax.plot(n, a_n, 'bo', linestyle='--', markerfacecolor='blue', label='$a_n = 1/n$')

    # Limite (inf = 0)
    ax.axhline(0, color='red', linestyle='-', linewidth=1.5, label='Limite L = inf A = 0')

    ax.set_xlabel('Indice n')
    ax.set_ylabel('Valore $a_n$')
    ax.set_title('Successione Decrescente (Teorema di Regolarità)')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    plt.show()

# Esecuzione dei plot
if __name__ == '__main__':
    plot_funzioni_iperboliche()
    plot_valore_assoluto()
    plot_potenze()
    plot_piano_gauss()
    plot_successione_decrescente()
