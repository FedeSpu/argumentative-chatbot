# Chatbot argomentativo

## Setup Chatbot Framework
I contesti di risposta del chatbot ("greetings",...) possono essere definiti nel file *intents.json* secondo la grammatica JSON. Per rendere effettive le modifiche bisogna
eseguire *MainProg.py*. 

## Setup Chatbot
Inserire i file presenti in una cartella (es. "tesi"). Per il corretto funzionamento del chatbot bisogna:
- Creare una cartella nello stesso path di "tesi" con il nome "**predictor**" e i file relativi a MARGOT portable al suo interno. Necessaria è la presenza del file 
"**run_margot.sh**"
- Creare una cartella "**DataSet**" con all'interno un file "**Evidence.csv**" con almeno la colonna "CDE" contenente le possibili risposte
Questi due passaggi sono contestuali all'utilizzo del chatbot così fornito. Ovviamente eventuali modifiche per l'esensione possono essere fatte sul codice.

## Funzionamento
Il programma funziona solo su Linux
1) Digitare su terminale "/venv/bin/python3.7 Gui.py" 
2) Aperto il programma, bisognerà digitare "margot" e inserire una frase argomentativa IN INGLESE (una sola verrà selezionata, anche in caso di più       
   argomentazioni)
3) Cliccare "Conferma". Se la casella (dopo alcuni secondi) scomparirà, l'operazione sarà andata a buon fine (proseguire punto 4), se invece il tasto conferma
   tornerà ad essere cliccabile, ma la casella non sarà scomparsa, allora nella vostra frase non è stata rilevata alcuna argomentazione. Chiudere il programma
   e tornare al punto 1).
4) Digitando "show" verranno mostrate 3 frasi correlate al vostro input. Scegliere quella che più si avvicina all'idea espressa nell'input, votando il numero
   corrispondente (la prima risposta mostrata avrà numero 1) nell'apposita barra che comparirà insieme alle risposte. Se la barra scompare, il vostro voto
   sarà andato a buon fine. 
5) È possibile ripetere i punti dal 2) al 4). Per terminare il programma basta digitare "bye"
