# Cum aplic la practica pentru Facebook, Google, Amazon...:

- Speaker: [bumbu](https://www.fb.com/bumbu) / [bumbu.me](https://bumbu.me)
- Date: 19.09.2018

## 0) Am dubii

Am scris cod, dar nu mult, doar cât am făcut laboratoare la universitate. Înțeleg unele structuri de date (array, linked list, stack, binary tree, graph) deși grafurile mi se dau mai greu. 

Dar am dubii că sunt destul de bun/ă penrtu o așa companie, poate voi aplica la anul. Totuși am dubii și îi scriu lui alex bumbu dacă are rost să aplic în acest an. El mă convinge că are rost și eu mă decid să încerc. **Nu am ce pierde, și in cel mai bun caz câștig experiență.**

## 1) Îmi pregătesc CVul

CVul va povesti istoria mea: experiențele, impactul și pasiunile. Evidențiaz realizările, dar sunt sincer/ă.

_Una din metode cum s-o faci_:
* La inceput scriu pe o hîrtie experiențele mele din domeniu. O simplă listă de:
  * practici/internships
  * lucru
  * proiecte de la start-upuri și hackathons
  * cursuri și laboratoare interesante
  * lucrari de laborator sau curs
* Le scriu pe toate, chiar și pe alea care nu par a fi deosebite.
* Pentru fiecare experiență încerc să scriu:
  * care a fost partea cea mai interesantă pentru mine
  * principalele tehnologii utilizate
  * care a fost impactul meu
  * URL (ex. Github) în caz ca sunt on-line
* Ordonez experiențele după ordinea în care aș vrea să fie citite (primul cel mai special pentru mine)
* Am cîteva experiențe la care nu am avut ce scrie, și am hotărît să le șterg pe alea care nu sunt exact relevante la domeniu (curs la filosofie, voluntariat la școală, proiect de curs la desen tehnic) dar le păstrez pe alea relevante (curs la structuri de date, laboratorul la calculus in care am implementat operațiuni aritmetice cu numere de lungime infinita)
* Acum am o lista de 3-7 experiențe cu descriere, si opțional cîteva experiențe fără descriere, dar care îmi par importante/interesante
* Acum partea ușoară:
  * Găsesc un oarecare șablon de CV 
  * Adaug datele de contact (nume, telefon, email)
  * Adaug Universitatea, Specialitatea și anul în care este preconizat să absolvesc
  * Adaug lista de experiențe pe care am scris-o anterior
  * [opțional] Adaug ca anotație lista de cursuri și notele care le-am obținut până astăzi
  

Spre exemplu la experiențe scriu:

### Big numbers arithmetic operations
In one of the calculus homeworks we had to find out what's the lowest floating point error that we could get in Matlab. I got interested in the topic and decided to test if it's possible to overcome this issue by implementing my own arithmetic operations by storing the digits in an array and simulating the operations that we normally do on paper. I got to a working solution, but found out that after having more than 1000 digits multiplication and division became too slow. But it was enough to have a more accurate result than what you get with 64bit numbers. 

### Cocos Media internship, Summer 2018
During this internship I worked on shipping the new logging for front-end layer (python) of the cocos media website (50k requests daily). New logging was consuming less resources which decreased avg server response time by 3%. One of the challenges was to have 0 downtime and no gaps in logging which I successfully achieved. I also made sure that logging is accounted for in E2E tests by updating few tests and creating documentation on how that should be done.

### Better Flappy Game, Feb-May 2018
github.com/bumbu/better-flappy
As part of Windows Programming course work I build a clone of Flappy Birds game (single-click only) using only native Windows API for graphics. This allowed me to understand better how the system works and how to create high-performing visual apps for any UI heavy applications. 
One of the challenges was memory consumption, and after investigating memory usage using VS Magic Memory I found the issue (garbage collection was too slow). After identifying 2 types of objects that caused 80% of regression, I used Objects Pool pattern that increased the frame rate from 10 to 60 fps.


## 2) Aplic

Aplic acum și mă voi pregăti in paralel. Nu mă limitez la o singură companie și aplic la mai multe:
* Facebook
  * Îl contactez pe bumbu, îi transmit email-ul personal și el îmi trimite referral
  * [sau] Îl contactez pe bumbu, îi transmit email-ul personal și menționez că aș vrea să fiu contactat de recruiter direct
  * [sau] Aplic direct de pe https://facebook.com/careers
* Google
  * Cunosc pe cineva cine lucreaza la Google și cer un referral
  * [sau] Îl contactez pe alex, menționez că mii interesant și Google, și el îmi dă contactele la un inginer care poate sa-mi dea un referral
  * [sau] Aplic direct de pe https://careers.google.com
* Amazon
  * Cunosc pe cineva cine lucreaza la Amazon și cer un referral
  * [sau] Îl contactez pe alex, menționez că mii interesant și Google, și el îmi dă contactele la un inginer care poate sa-mi dea un referral
  * [sau] Aplic direct de pe https://www.amazon.jobs/en/business_categories/university-recruiting
* Compania mea de vis (Netflix, Dropbox, Asana, Uber...)
  * Verific dacă au poziții deschise penru practică și aplic și acolo


## 3) Mă pregătesc pentru interviuri

* Zilnic încerc să comunic cu colegii/prietenii/motanul în engleză pentru a mă simți confortabil să duc un dialog tehnic in engleză
* Mă focusez minim pe următorii algoritmi, structuri de date de bază:
  * _Pentru fiecare algoritm înțeleg care e complexiteatea de timp și spațiu_
  * Liste: array, linked list (single, double), stack, queue, heap, set, hash/dictionary
  * Trees: binary tree, binary search tree, trie, breadth first (Bfs) și depth first (Dfs) search/traversal in trees
  * Graphs: Bfs, Dfs
* Îmi aleg o carte/on-line și studiez/revăd structurile de date și algoritmii de bază. Câteva cărți bune:
  * [Cracking the Coding Interview](http://amzn.to/2y5W5qV)
  * [Introduction to algorithms](http://amzn.to/2h7i1hW)
  * [The Algorithm Design Manual](http://amzn.to/2y6ueaa)
* Mă înregistrez pe https://www.interviewbit.com/ și trec primele 6 nivele de la Practice/Programming
* Împreună cu colegul/colega mea de grupă simulăm un interviu (cel puțin 2 ori)
  * Eu voi fi interviator [1] și voi alege o problemă din carte sau de pe interviewbit, și în decurs la inverviu îmi voi nota pe o hârtie toate sugestiile/greșelile
  * Colegul va fi interviatul [2]
  * [1] Eu dau întrebarea (e.g. Determină dacă 2 cuvinte sunt anagrame)
  * [2] Colegul îmi dă întrebări de clarificare (e.g. ce e o anagramă, dacă simbolurile sunt ASCII sau UTF-8, care e mărimea maximă la string...)
  * [1] Eu aleg aleator și răspund aceste întrebări
  * [2] Colegul ia câteva exemple (e.g. "mar" și "arm" sau, "face" si "faces" și le scrie in colțul drept al tablei să le aibă ca exemple)
  * [2] Colegul se gândește la prima soluție care îi vine în cap și o spune în voce (e.g. sortăm ambele stringuri, apoi iterăm prin primul și comparăm dacă caracterele din aceiași poziție din al 2-lea string coincid). El îmi spune care este complexitatea de timp și spațiu (O(n log n) ca timp, O(1) spațiu dacă algoritmul de sortare e "in place sorting")
  * [2] Colegul se gândește dacă acest algoritm ar putea fi optimizat ca timp. Găsește o altă soluție care va reduce complexitatea la timp dar va mări complexitatea la spațiu. 
  * [2] Colegul întreabă ce este mai important în cazul acestei probleme (timpul sau spațiul) și alege respectiv una din aceste soluții
  * [1] Eu îi spun că timpul e mai important
  * [2] Colegul scrie soluția la tablă
  * [2] După ce soluția e scrisă, el folosește exemplele care le-a scris anterior ca să verifice corectitudinea la algoritm
  * [2] A găsit o greșeală și corectează greșeala
  * [1] Dacă eu văd vreo greșeală conceptuală, sau un exemplu care ar mai scoate la iveală vreo greșeala - îl rog să încerce acest exemplu
  * [1] Menționez toate notițele relevante (e.g. "Ai uitat să dai întrebări de clarificare la început" sau "Ai greșit complexitatea de timp la prima soluție")
  * Acum ne schimbăm cu rolurile.
* Partea cea mai importantă: practic cu oameni necunoscuți:
  * Mă înregistrez pe [pramp.com](https://www.pramp.com/)
  * Fac cel puțin 3 interviuri pe platformă

## 4) Interviul

Dorm bine înainte de ziua în care am interviu. 

Trec superficial prin structuri de date și algoritmi. 

În ziua în care am interviu telefonic, sunt și calm dar și excitat doar prin faptul că deja am acumulat un set util de experiențe. Sunt conștient că acest interviu poate să nu fie de succes, dar știu că e unica metodă de a învăță. 
**Și chiar dacă nu-mi reușește acest interviu sau acest an, o să știu la ce să mă pregătesc pentru anul viitor.**
