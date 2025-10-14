import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from fractions import Fraction

# --- Funzione Helper per l'impostazione degli assi ---
def setup_axes(xtick=np.pi/2, ytick=0.5, xlabels_as_pi=True):
    """Imposta assi cartesiani con griglia e tick personalizzati."""
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(True, linestyle="--", linewidth=0.5)

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    # Tick asse x
    if xlabels_as_pi:
        ticks = np.arange(-2*np.pi, 2.5*np.pi, xtick)
        labels = []
        for t in ticks:
            if np.isclose(t, 0):
                labels.append(r"$0$")
            elif np.isclose(t, np.pi):
                labels.append(r"$\pi$")
            elif np.isclose(t, -np.pi):
                labels.append(r"$-\pi$")
            else:
                frac = Fraction(t/np.pi).limit_denominator(8)
                num, den = frac.numerator, frac.denominator
                if num == 1 and den == 1:
                    labels.append(r"$\pi$")
                elif den == 1:
                    labels.append(r"$%d\pi$" % num)
                else:
                    labels.append(r"$\frac{%d\pi}{%d}$" % (num, den))
        plt.xticks(ticks, labels)
    else:
        plt.xticks(np.arange(xmin, xmax+xtick, xtick))

    # Tick asse y
    plt.yticks(np.arange(ymin, ymax+ytick, ytick))


# --- Funzioni di plotting ---

def circonferenza_goniometrica():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    setup_axes(xtick=0.5, ytick=0.5, xlabels_as_pi=False)

    circle = patches.Circle((0, 0), radius=1, fill=False, color='blue', linewidth=2)
    ax.add_patch(circle)

    angles = {
        r'$\frac{\pi}{6}$': np.pi/6, r'$\frac{\pi}{4}$': np.pi/4, r'$\frac{\pi}{3}$': np.pi/3,
        r'$\frac{2\pi}{3}$': 2*np.pi/3, r'$\frac{3\pi}{4}$': 3*np.pi/4, r'$\frac{5\pi}{6}$': 5*np.pi/6
    }

    for label, angle in angles.items():
        x_end = np.cos(angle)
        y_end = np.sin(angle)
        ax.plot([0, x_end], [0, y_end], color='red', linestyle='-')
        ax.text(x_end * 1.2, y_end * 1.2, label, fontsize=14, ha='center', va='center')

    plt.savefig("./img/circonferenza_goniometrica.png", dpi=300, bbox_inches='tight')
    plt.close(fig)


def seno_coseno_grafici():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(-2*np.pi, 2*np.pi, 500)
    ax.plot(x, np.sin(x), label=r'$y=\sin(x)$', color='blue')
    ax.plot(x, np.cos(x), label=r'$y=\cos(x)$', color='orange')

    ax.set_xlim(-2*np.pi, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    setup_axes(xtick=np.pi/2, ytick=0.5, xlabels_as_pi=True)
    ax.legend()
    plt.savefig("./img/seno_coseno_grafici.png", dpi=300, bbox_inches='tight')
    plt.close(fig)


def tangente():
    fig, ax = plt.subplots(figsize=(6, 6))
    x = np.linspace(-np.pi, np.pi, 1000)
    y = np.tan(x)

    # Evita discontinuità
    mask = np.zeros_like(y, dtype=bool)
    mask[:-1] = np.abs(np.diff(y)) > 10
    y[mask] = np.nan
    ax.plot(x, y, color='green')

    ax.axvline(x=-np.pi/2, color='gray', linestyle='--')
    ax.axvline(x=np.pi/2, color='gray', linestyle='--')

    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-5, 5)
    setup_axes(xtick=np.pi/4, ytick=1, xlabels_as_pi=True)

    plt.savefig("./img/tangente.png", dpi=300, bbox_inches='tight')
    plt.close(fig)


def arcsin_arccos_grafici():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(-1, 1, 500)
    ax.plot(x, np.arcsin(x), label=r'$y=\arcsin(x)$', color='blue')
    ax.plot(x, np.arccos(x), label=r'$y=\arccos(x)$', color='orange')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-np.pi/2 - 0.5, np.pi + 0.5)
    setup_axes(xtick=0.5, ytick=np.pi/4, xlabels_as_pi=False)
    ax.legend()
    plt.savefig("./img/arcsin_arccos_grafici.png", dpi=300, bbox_inches='tight')
    plt.close(fig)


def arcotangente():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(-10, 10, 500)
    ax.plot(x, np.arctan(x), color='purple')

    ax.axhline(y=-np.pi/2, color='gray', linestyle='--')
    ax.axhline(y=np.pi/2, color='gray', linestyle='--')

    ax.set_xlim(-6, 6)
    ax.set_ylim(-np.pi, np.pi)
    setup_axes(xtick=1, ytick=np.pi/4, xlabels_as_pi=False)

    plt.savefig("./img/arcotangente.png", dpi=300, bbox_inches='tight')
    plt.close(fig)


# --- Esecuzione dello script ---
if __name__ == "__main__":
    import os
    if not os.path.exists("./img"):
        os.makedirs("./img")
    
    print("Generazione immagini in corso...")
    circonferenza_goniometrica()
    seno_coseno_grafici()
    tangente()
    arcsin_arccos_grafici()
    arcotangente()
    print("Tutte le immagini sono state generate nella cartella 'img'.")
