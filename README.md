# CercaLavori_Remoti
Script che fa scraping nei motori di ricerca e individua gli annunci di lavoro remoti

# esempio di utilizzo

python3 cercalavoro.py

una volta lanciato il comando viene richiesto all'utente il tipo di lavoro cercato..

Esempi di ricerca: python, sql, react ecc.. nel caso si cercasse più parole insieme mettere le virgolette esempio "social media manager"

Di default lo script stampa gli url individuati a schermo, nel caso si volesse fare l'output il comando è il seguente:

python3 cercalavoro.py -o (CSV,JSON,HTML) -n nomedelfile

in caso si trovassero pochi risultati provare ad inserire il seguente parametro -e all

esempio:
python3 cercalavoro.py -o csv -n lavoriestratti -e all


#installazione

scaricare e scompattare lo zip
Python3 setup.py install

è ovviamente necessario avere python installato.
