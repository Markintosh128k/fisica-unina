import os
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# ----------------------------------------------------------------------
# Configurazione
# ----------------------------------------------------------------------
CARTELLA_IMMAGINI = "img"
NOMI_FILE_RICHIESTI = {
    "esempio8_succ_numeriche.jpg": "Grafico del perimetro del poligono inscritto (convergenza a 2piR)",
    "lim_succ_num.jpg": "Definizione generale del Limite (a_n -> l con epsilon-nu)",
    "successione_1-su-n.jpg": "Successione an = 1/n",
    "succ_a_n=n.jpg": "Successione an = n",
    "succ_osc_1_-1.jpg": "Successione oscillante an = (-1)^n",
    "intervalli_unicita_lim.jpg": "Dimostrazione unicità del limite (Intorni disgiunti)"
}

# Imposta Matplotlib per uno stile pulito e adatto ai documenti
plt.style.use('default')

# ----------------------------------------------------------------------
# Funzioni di Plotting Specifiche
# ----------------------------------------------------------------------

def plot_perimetro_poligono(filepath):
    """Plotta la convergenza del perimetro P_n = 2nR sin(pi/n) a 2piR."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Raggio per semplicità (R=1). Limite = 2 * pi * 1 ≈ 6.28
    R = 1
    
    # Punti della successione: n da 3 a 50
    n = np.arange(3, 51)
    a_n = 2 * n * R * np.sin(pi / n)
    limite = 2 * pi * R
    
    # Plot della successione
    ax.plot(n, a_n, 'bo-', markersize=3, label='$P_n = 2nR \\sin(\\frac{\\pi}{n})$')
    
    # Plot del limite (circonferenza)
    ax.axhline(limite, color='r', linestyle='--', label='Limite $2\\pi R$')
    
    ax.set_title("Convergenza del Perimetro del Poligono Inscritto")
    ax.set_xlabel('$n$ (numero lati)')
    ax.set_ylabel('$P_n$')
    ax.set_ylim(4.5, limite * 1.05)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    fig.savefig(filepath, format='jpg', dpi=200)
    plt.close(fig)

def plot_limite_generale(filepath):
    """Illustra la definizione di limite (epsilon-nu) usando a_n = 1/n."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    n = np.arange(1, 20)
    a_n = 1 / n
    l = 0
    epsilon = 0.3
    
    # Plot del limite e della striscia epsilon
    ax.axhline(l, color='r', linestyle='-', linewidth=1.5, label='Limite $l$')
    ax.axhspan(l - epsilon, l + epsilon, color='orange', alpha=0.3, label='$(l-\\epsilon, l+\\epsilon)$')
    
    # Plot della successione
    ax.plot(n, a_n, 'ko', markersize=4, label='$a_n$')
    ax.vlines(n, 0, a_n, color='k', linestyle=':', alpha=0.4)
    
    # Evidenziazione del nu
    nu = int(1 / epsilon) + 1  # n > 1/epsilon
    ax.axvline(nu, color='g', linestyle='-.', label='Soglia $\\nu$')
    
    ax.set_title("Rappresentazione del Limite ($\epsilon-\\nu$)", fontsize=10)
    ax.set_xlabel('$n$', fontsize=10)
    ax.set_yticks([l - epsilon, l, l + epsilon])
    ax.set_yticklabels(['$l-\\epsilon$', '$l$', '$l+\\epsilon$'])
    ax.set_xticks([nu])
    ax.set_xticklabels(['$\\nu$'])
    ax.legend(loc='upper right')
    ax.set_xlim(0.5, 20)
    fig.savefig(filepath, format='jpg', dpi=200)
    plt.close(fig)

def plot_un_su_n(filepath):
    """Plotta la successione a_n = 1/n."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    n = np.arange(1, 15)
    a_n = 1 / n
    
    ax.plot(n, a_n, 'ko-', markersize=4, label='$a_n = 1/n$')
    ax.axhline(0, color='r', linestyle='--', label='Limite $l=0$')
    
    ax.set_title("Successione $a_n = 1/n$ (Infinitesima)")
    ax.set_xlabel('$n$')
    ax.set_ylabel('$a_n$')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, linestyle=':', alpha=0.6)
    fig.savefig(filepath, format='jpg', dpi=200)
    plt.close(fig)

def plot_an_uguale_n(filepath):
    """Plotta la successione a_n = n."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    n = np.arange(1, 10)
    a_n = n
    
    ax.plot(n, a_n, 'bo-', markersize=4, label='$a_n = n$')
    
    ax.set_title("Successione $a_n = n$ (Divergente a $+\\infty$)")
    ax.set_xlabel('$n$')
    ax.set_ylabel('$a_n$')
    ax.grid(True, linestyle=':', alpha=0.6)
    fig.savefig(filepath, format='jpg', dpi=200)
    plt.close(fig)

def plot_succ_oscillante(filepath):
    """Plotta la successione oscillante a_n = (-1)^n."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    n = np.arange(1, 15)
    a_n = (-1)**n
    
    ax.plot(n, a_n, 'ro', linestyle='--', markersize=5, label='$a_n = (-1)^n$')
    
    ax.set_title("Successione $a_n = (-1)^n$ (Irregolare / Oscillante)")
    ax.set_xlabel('$n$')
    ax.set_ylabel('$a_n$')
    ax.set_yticks([-1, 0, 1])
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, linestyle=':', alpha=0.6)
    fig.savefig(filepath, format='jpg', dpi=200)
    plt.close(fig)

def plot_unicita_limite(filepath):
    """Illustra gli intorni disgiunti per la dimostrazione di unicità del limite."""
    fig, ax = plt.subplots(figsize=(6, 2))
    
    l1 = 1
    l2 = 3
    a = 2  # Punto di separazione
    
    # Plot Intorno I(l1) = ]-\infty, a[
    ax.hlines(0, -1, a, color='blue', linewidth=8, alpha=0.5, label='$I(l_1)$')
    # Plot Intorno I(l2) = ]a, +\infty[
    ax.hlines(0, a, 5, color='red', linewidth=8, alpha=0.5, label='$I(l_2)$')
    
    # Mark l1, l2, and a
    ax.plot(l1, 0, 'go', markersize=8, label='$l_1$')
    ax.plot(l2, 0, 'go', markersize=8, label='$l_2$')
    ax.plot(a, 0, 'kx', markersize=8, mew=2, label='$a$')
    
    ax.set_title("Intorni Disgiunti ($I(l_1) \\cap I(l_2) = \\emptyset$)")
    ax.set_yticks([])
    ax.set_xticks([l1, a, l2])
    ax.set_xticklabels(['$l_1$', '$a$', '$l_2$'])
    ax.set_ylim(-0.2, 0.2)
    ax.set_xlim(0, 4)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    # Rimuovi l'asse y
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    fig.savefig(filepath, format='jpg', dpi=200, bbox_inches='tight')
    plt.close(fig)

# ----------------------------------------------------------------------
# Mappa di Associazione File -> Funzione
# ----------------------------------------------------------------------

MAPPA_GENERAZIONE = {
    "esempio8_succ_numeriche.jpg": plot_perimetro_poligono,
    "lim_succ_num.jpg": plot_limite_generale,
    "successione_1-su-n.jpg": plot_un_su_n,
    "succ_a_n=n.jpg": plot_an_uguale_n,
    "succ_osc_1_-1.jpg": plot_succ_oscillante,
    "intervalli_unicita_lim.jpg": plot_unicita_limite
}

# ----------------------------------------------------------------------
# Funzione Principale
# ----------------------------------------------------------------------

def genera_grafici_sicuro():
    """Itera e genera i grafici solo se non esistono già, nella cartella specificata."""
    
    if not os.path.isdir(CARTELLA_IMMAGINI):
        print(f"\n❌ ERRORE: La cartella '{CARTELLA_IMMAGINI}' NON è stata trovata.")
        print("   Per favore, crea la cartella 'img/' prima di eseguire lo script.")
        return

    print("Inizio la generazione dei grafici...")
    print("-------------------------------------------")

    creati = 0
    esistenti = 0
    
    for nome_file, funzione_plot in MAPPA_GENERAZIONE.items():
        percorso_completo = os.path.join(CARTELLA_IMMAGINI, nome_file)
        descrizione = NOMI_FILE_RICHIESTI[nome_file]
        
        if os.path.exists(percorso_completo):
            print(f"   - Saltato: '{nome_file}'. Il file esiste già.")
            esistenti += 1
        else:
            try:
                funzione_plot(percorso_completo)
                print(f"   - Creato: '{nome_file}' ({descrizione})")
                creati += 1
            except Exception as e:
                print(f"   - ERRORE grave durante la creazione di '{nome_file}': {e}")
                
    print("\n-------------------------------------------")
    print("✅ Completato! Dettagli dell'operazione:")
    print(f"   - Grafici creati: {creati}")
    print(f"   - File esistenti (saltati): {esistenti}")
    if creati > 0:
        print("\nNota: I file sono stati salvati come .jpg. Se desideri una qualità superiore e file più piccoli (generalmente raccomandato per i grafici), puoi cambiare il formato in .png all'interno dello script.")

if __name__ == "__main__":
    genera_grafici_sicuro()