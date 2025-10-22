# fisica-unina

Questo repository contiene appunti, eserciziari e materiale didattico per il corso di Fisica (Canale 1, A-G) dell'Università di Napoli Federico II.

## Struttura del Repository

Il materiale è organizzato per materia:

* **/Analisi I**:
    * `Appunti`: Note del corso in formato LaTeX e PDF.
    * `Eserciziari`: Raccolte di esercizi (es. Marcellini-Sbordone, Alvino-Trombetti).
    * `Libri`: Testi di riferimento consigliati.

* **/Laboratorio di Fisica I**:
    * Materiale ed esperienze di laboratorio.

### Compilazione

Per compilare i file `.tex` (ad esempio `Analisi I/Appunti/analisi_1.tex`):

1.  Assicurati di avere una distribuzione LaTeX installata (es. TeX Live, MiKTeX).
2.  I file principali dipendono da `theorems.tex` e `commands.tex`, che devono trovarsi nella stessa directory o in una directory inclusa nel percorso di ricerca di LaTeX.
3.  Compila il file sorgente (es. `pdflatex analisi_1.tex`). Potrebbero essere necessarie più compilazioni per risolvere i riferimenti incrociati e la tabella dei contenuti.

### Template

Nella root del repository è presente un file `template.tex` che può essere utilizzato come base per creare nuovi documenti mantenendo lo stesso stile e formattazione degli appunti.