import numpy as np
import matplotlib.pyplot as plt

# Configurazione generale dei plot
plt.style.use('default')
# Stile per la funzione di base (tratteggiata, grigia)
BASE_STYLE = {'linestyle': '--', 'color': 'gray', 'label': '$f(x)$', 'alpha': 0.7}
# Stile per la funzione trasformata (continua, rossa)
TRANS_STYLE = {'linestyle': '-', 'color': 'red', 'linewidth': 2}

# Definiamo una funzione di base che non sia né pari né dispari
# f(x) = x^3 - x^2 - 2x
def f(x):
    """Funzione di base per le trasformazioni."""
    return x**3 - x**2 - 2*x

# Range X e Y di base
x_base = np.linspace(-2.5, 3.5, 400)
y_base = f(x_base)

# Costanti per le trasformazioni
K_trasl = 1.5 # Per traslazioni
K_dil = 2.0   # Per dilatazioni

# Funzione helper per impostare assi, griglia e titolo
def setup_plot(ax, title, ylim=None):
    """Imposta elementi comuni del grafico (assi, griglia, titolo, legenda)."""
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(title)
    ax.legend(loc='upper left')
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])

# 1. Traslazione Verticale
def plot_traslazione_verticale():
    """Grafico per f(x) + K"""
    y_trans = f(x_base) + K_trasl

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x_base, y_base, **BASE_STYLE)
    ax.plot(x_base, y_trans, **TRANS_STYLE, label=f'$f(x) + {K_trasl}$')
    setup_plot(ax, '1. Traslazione Verticale ($f_1(x) = f(x) + K$)', [-10, 15])
    plt.savefig("traslazione_verticale.png")


# 2. Traslazione Orizzontale
def plot_traslazione_orizzontale():
    """Grafico per f(x + K) (shift a sinistra)"""
    # Usiamo K positivo (x + K) per uno shift a sinistra
    y_trans = f(x_base + K_trasl)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x_base, y_base, **BASE_STYLE)
    ax.plot(x_base, y_trans, **TRANS_STYLE, label=f'$f(x + {K_trasl})$')
    setup_plot(ax, '2. Traslazione Orizzontale ($f_2(x) = f(x + K)$)', [-10, 15])
    plt.savefig("traslazione_orizzontale.png")


# 3. Dilatazione/Contrazione (Mostra entrambi K f(x) e f(K x))
def plot_dilatazione():
    """Grafico per K f(x) e f(K x)"""
    y_trans_vert = K_dil * f(x_base)  # Dilatazione verticale
    y_trans_horiz = f(K_dil * x_base) # Contrazione orizzontale

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('3. Dilatazione/Contrazione', fontsize=16)

    # Subplot 1: K f(x)
    ax1.plot(x_base, y_base, **BASE_STYLE)
    ax1.plot(x_base, y_trans_vert, **TRANS_STYLE, label=f'${K_dil} f(x)$')
    setup_plot(ax1, 'Dilatazione Verticale ($K f(x)$)', [-15, 20])

    # Subplot 2: f(K x)
    ax2.plot(x_base, y_base, **BASE_STYLE)
    ax2.plot(x_base, y_trans_horiz, **TRANS_STYLE, label=f'$f({K_dil} x)$')
    setup_plot(ax2, 'Contrazione Orizzontale ($f(K x)$)', [-10, 15])

    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    plt.savefig("dilatazione.png")


# 4. Ribaltamento Rispetto all'asse x
def plot_ribaltamento_x():
    """Grafico per -f(x)"""
    y_trans = -f(x_base)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x_base, y_base, **BASE_STYLE)
    ax.plot(x_base, y_trans, **TRANS_STYLE, label='$-f(x)$')
    setup_plot(ax, "4. Ribaltamento Asse x ($f_4(x) = -f(x)$)", [-15, 15])
    plt.savefig("ribaltamento_x.png")


# 5. Ribaltamento Rispetto all'asse y
def plot_ribaltamento_y():
    """Grafico per f(-x)"""
    y_trans = f(-x_base)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x_base, y_base, **BASE_STYLE)
    ax.plot(x_base, y_trans, **TRANS_STYLE, label='$f(-x)$')
    setup_plot(ax, "5. Ribaltamento Asse y ($f_5(x) = f(-x)$)", [-10, 20])
    plt.savefig("ribaltamento_y.png")

# 6. Valore Assoluto Esterno
def plot_valore_assoluto_esterno():
    """Grafico per |f(x)|"""
    y_trans = np.abs(f(x_base))

    fig, ax = plt.subplots(figsize=(7, 5))
    # Mostra la base f(x) originale
    ax.plot(x_base, y_base, **BASE_STYLE)
    # Mostra la trasformazione |f(x)|
    ax.plot(x_base, y_trans, **TRANS_STYLE, label='$|f(x)|$')
    setup_plot(ax, '6. Valore Assoluto Esterno ($f_6(x) = |f(x)|$)', [-5, 15])
    plt.savefig("valore_assoluto_esterno.png")


# 7. Valore Assoluto Interno
def plot_valore_assoluto_interno():
    """Grafico per f(|x|)"""
    y_trans = f(np.abs(x_base))

    fig, ax = plt.subplots(figsize=(7, 5))

    # Per f(|x|), la parte per x<0 viene "cancellata"
    ax.plot(x_base[x_base < 0], y_base[x_base < 0],
            linestyle='--', color='lightgray', label='$f(x)$ (per $x < 0$, ignorata)', alpha=0.7)

    # La parte per x>0 viene usata e riflessa
    ax.plot(x_base[x_base >= 0], y_base[x_base >= 0],
            linestyle=':', color='blue', label='$f(x)$ (per $x \geq 0$, riflessa)')

    # Questo è il risultato f(|x|)
    ax.plot(x_base, y_trans, **TRANS_STYLE, label='$f(|x|)$ (risultato)')

    setup_plot(ax, '7. Valore Assoluto Interno ($f_7(x) = f(|x|)$)', [-5, 15])
    plt.savefig("valore_assoluto_interno.png")


# --- Esecuzione di tutti i plot ---
if __name__ == '__main__':
    print("Generazione grafico 1: Traslazione Verticale")
    plot_traslazione_verticale()

    print("Generazione grafico 2: Traslazione Orizzontale")
    plot_traslazione_orizzontale()

    print("Generazione grafico 3: Dilatazione/Contrazione")
    plot_dilatazione()

    print("Generazione grafico 4: Ribaltamento Asse x")
    plot_ribaltamento_x()

    print("Generazione grafico 5: Ribaltamento Asse y")
    plot_ribaltamento_y()

    print("Generazione grafico 6: Valore Assoluto Esterno")
    plot_valore_assoluto_esterno()

    print("Generazione grafico 7: Valore Assoluto Interno")
    plot_valore_assoluto_interno()
