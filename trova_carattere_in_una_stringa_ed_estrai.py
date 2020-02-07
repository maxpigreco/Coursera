data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'    #stringa in cui fare ricerca
print(data)                                                         #stampa la stringa a video
posizione_iniziale = data.find('@')                                 #cerca il primo carattere del testo da estrarre 
print("Posizione iniziale: ", posizione_iniziale)
    
posizione_spazio = data.find(' ', posizione_iniziale)               #trovare dove termina il testo da estrarre
print("Posizione spazio: ", posizione_spazio)                       #lo stampa

host = data[posizione_iniziale+1:posizione_spazio]                  #assegno la variabile host al testo da estrarre
print("Host: ", host)                                               #stampo il testo estratto
