import numpy as np
import matplotlib.pyplot as plt
import cmath
import os

# Configurazione generale dei plot
plt.style.use('default')

# Definizione della directory per il salvataggio
OUTPUT_DIR = "img"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 1. Funzioni Iperboliche (Lezione 12)
def plot_funzioni_iperboliche():
    x = np.linspace(-3, 3, 400)
    sinh_x = np.sinh(x)
    cosh_x = np.cosh(x)

    # --- Plot 1: Seno Iperbolico (sinh x) ---
    fig_sinh, ax_sinh = plt.subplots(figsize=(6, 5))
    ax_sinh.plot(x, sinh_x, label=r'$\sinh(x)$', color='red')
    ax_sinh.plot(x, np.exp(x)/2, '--', color='gray', alpha=0.5, label=r'$e^x/2$')
    ax_sinh.plot(x, -np.exp(-x)/2, ':', color='black', alpha=0.5, label=r'$-e^{-x}/2$')
    ax_sinh.axhline(0, color='black', linewidth=0.5)
    ax_sinh.axvline(0, color='black', linewidth=0.5)
    ax_sinh.set_title(r'Grafico di Seno Iperbolico ($\sinh x$)')
    ax_sinh.set_ylim(-10, 10)
    ax_sinh.legend()
    plt.savefig(os.path.join(OUTPUT_DIR, 'grafico_senh.png'))
    plt.close(fig_sinh)

    # --- Plot 2: Coseno Iperbolico (cosh x) ---
    fig_cosh, ax_cosh = plt.subplots(figsize=(6, 5))
    ax_cosh.plot(x, cosh_x, label=r'$\cosh(x)$', color='red')
    ax_cosh.plot(x, np.exp(x)/2, '--', color='blue', alpha=0.5)
    ax_cosh.plot(x, np.exp(-x)/2, ':', color='green', alpha=0.5)
    ax_cosh.axhline(0, color='black', linewidth=0.5)
    ax_cosh.axvline(0, color='black', linewidth=0.5)
    ax_cosh.set_title(r'Grafico di Coseno Iperbolico ($\cosh x$)')
    ax_cosh.set_ylim(0, 10)
    ax_cosh.legend()
    plt.savefig(os.path.join(OUTPUT_DIR, 'grafico_cosh.png'))
    plt.close(fig_cosh)

    # Nota: Il placeholder 'iperbole_e_sett.png' è generico, lo gestiamo con un grafico unificato o ne saltiamo la generazione diretta.
    # Generiamo un placeholder semplice per le inverse (settore)
    fig_sett, ax_sett = plt.subplots(figsize=(6, 5))
    x_sett = np.linspace(-3, 3, 400)
    ax_sett.plot(x_sett, np.arcsinh(x_sett), label=r'$\operatorname{sett}\sinh x$')
    ax_sett.set_title(r'Funzione Inversa Iperbolica')
    ax_sett.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(os.path.join(OUTPUT_DIR, 'iperbole_e_sett.png'))
    plt.close(fig_sett)


# 2. Trasformazioni (Lezione 12/Cap. 3)
def plot_trasformazioni_grafico():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    f_x = np.sin(x)  # Funzione base: seno
    f_abs_ext = np.abs(f_x) # Valore assoluto esterno

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, f_x, label=r'$f(x) = \sin(x)$', color='blue')
    ax.plot(x, f_abs_ext, label=r'$|f(x)| = |\sin(x)|$', color='red', linestyle='--')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title('Trasformazione: Valore Assoluto Esterno')
    ax.legend()

    # Salviamo l'immagine
    plt.savefig(os.path.join(OUTPUT_DIR, 'trasformazioni_grafico.png'))
    plt.close(fig)

# 3. Piano di Gauss (Numeri Complessi - Lezione 13)
def plot_piano_gauss():
    z = complex(3, 4)
    rho = abs(z)

    fig, ax = plt.subplots(figsize=(6, 6))

    # Assi cartesiani
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)

    # Punto z
    ax.plot(z.real, z.imag, 'ro', label=f'$z = {z.real} + {z.imag}i$')

    # Vettore e Modulo
    ax.plot([0, z.real], [0, z.imag], 'b--', label=f'Modulo $|z| = {rho:.2f}$')

    ax.set_xlabel('Reale (a)')
    ax.set_ylabel('Immaginario (b)')
    ax.set_title('Piano di Gauss e Modulo')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

    # Salviamo l'immagine per "piano_gauss.png" e "forma_trigonometrica.png" (usiamo lo stesso plot per entrambi i concetti)
    plt.savefig(os.path.join(OUTPUT_DIR, 'piano_gauss.png'))
    plt.close(fig)

# 4. Successione Decrescente (Esempio 1/n - Lezione 15)
def plot_successione_decrescente():
    n = np.arange(1, 15)
    a_n = 1 / n

    fig, ax = plt.subplots(figsize=(8, 5))

    # Grafico della successione: punti discreti
    ax.plot(n, a_n, 'bo', linestyle='--', markerfacecolor='blue', label=r'$a_n = 1/n$')

    # Limite (inf = 0)
    ax.axhline(0, color='red', linestyle='-', linewidth=1.5, label='Limite $L = \inf A = 0$')

    ax.set_xlabel('Indice n')
    ax.set_ylabel(r'Valore $a_n$')
    ax.set_title('Successione Monotona Decrescente')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()

    # Salviamo l'immagine (usando il nome del placeholder generico che abbiamo in mente per le successioni)
    # Ho usato un nome logico non specificato nel LaTeX precedente, ma utile
    plt.savefig(os.path.join(OUTPUT_DIR, 'grafico_successione_monotona.png'))
    plt.close(fig)


if __name__ == '__main__':
    print(f"Generating graphs and saving them to the '{OUTPUT_DIR}' directory...")
    plot_funzioni_iperboliche()
    plot_trasformazioni_grafico()
    plot_piano_gauss()
    plot_successione_decrescente()
    print("Graph generation complete.")
