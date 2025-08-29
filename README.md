# PDF Merger - Fronti e Retro 📄✨

Ciao! 👋 Questo tool ti permette di unire due PDF (uno con le pagine di fronte e uno con quelle del retro) creando file PDF separati per ogni coppia di pagine. Perfetto per quando hai scansionato documenti fronte/retro e vuoi riunirli! 🖨️

## Come funziona 🚀

L'app prende due PDF:
- **PDF Fronti**: contiene tutte le pagine frontali (1, 3, 5, 7...)
- **PDF Retro**: contiene tutte le pagine del retro (2, 4, 6, 8...)

E crea dei PDF individuali dove ogni file contiene una pagina fronte + la sua corrispondente pagina retro! 📑

## Installazione 💻


> **Nota:** `tkinter`, `os`, `json`, `pathlib`, `random`, `string` sono già inclusi in Python! 🐍

## Come usare 🎯

1. **Avvia il programma**: `python main.py`
2. **Seleziona PDF Fronti**: clicca e scegli il file con le pagine frontali
3. **Seleziona PDF Retro**: clicca e scegli il file con le pagine del retro  
4. **Seleziona Cartella Output**: dove salvare i file risultanti
5. **Elabora PDF**: magia! ✨

L'app ricorda automaticamente la cartella di output per la prossima volta! 💾

## Caratteristiche fighe 😎

- ✅ **Interfaccia semplice** con tkinter
- ✅ **Salvataggio automatico** delle preferenze
- ✅ **Nomi casuali** per evitare sovrascritture
- ✅ **Controllo errori** se i PDF hanno pagine diverse
- ✅ **Status in tempo reale** dei file selezionati

## Struttura file 📂

Il programma salva le preferenze in:
- **Windows**: `C:\Users\TuoNome\.pdfmerger\preferenze.json`
- **Linux/Mac**: `~/.pdfmerger/preferenze.json`

I file di output hanno nomi casuali di 15 caratteri per evitare conflitti! 🎲

Happy merging! 🚀📄
