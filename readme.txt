Gasiti in acest repository urmatoarele directoare: 
- backup_intrari: locatia unde sunt mutate fisierele in urma rularii testului 1 
- input_fiels: locatia unde sunt salvate fisierele de test 
- intrari: locatia unde programul vostru va trebui sa "asculte" pentru fisiere noi
- main.py: acest fisier simuleaza fisierul vostru main.py si a fost folosit in scopul testarii checkerului 
- test.py: principalul fisier al checkerului. acesta initiaza rularea testelor 

Contributii: 
In cazul in care doriti sa contribuiti la acest checker, puteti sa creati un nou branch, sa modificati codul si apoi sa creati un Pull Request. 
Asteptati pentru aprobarea acestuia si apoi putem finaliza merge-ul branchului vostru cu main. 

Cerinte pe care le verificam: 
Scrieti un program python care permite monitorizarea orelor lucrate de angajatii unei companii. Datele pe care le primiti ca parametru provin de la punctele de access dintr-o cladire de birouri. Orice persoana, pentru a intra in cladire, sau pentru a iesi, trebuie sa valideze cardul de acces. Prin validare, se obtine id-ul persoanei care detine cartela, ora validarii precum si sensul (intrare sau iesire). 
In cladire pot exista 2 tipuri de porti prin care se face accesul. Primul tip salveaza toate aceste date intr-un fisier text sau csv care au aceeasi structura precum exemplele atasate. Al doilea tip de poarta, transmite in timp real catre server intrarile si iesirile prin internet, in format json. 
Cerinte: 
•	Creati un repository pe github (trebuie sa il faceti public pentru a incepe un portofoliu de aplicatii care va poate fi util la viitoare interviuri de angajare). Incarcati acolo tot codul pe care il dezvoltati. Va fi nevoie de un pull request pentru fiecare functionalitate implementata. 
•	In cadrul dezvoltarii folositi conceptele POO (incapsulare, mostenire, polimorfism, abstractizare)
•	Creati o functionalitate prin care un administrator poate inregistra utilizatori. Utilizatorii vor fi salvati intr-o tabela a bazei de date unde vom inregistra ID,Nume,Prenume, Companie, IdManager. Aceste detalii sunt transmise prin intermediul unui request prin care se transmit toate detaliile necesare. 
•	Primul tip de poarta: In cadrul proiectului va exista un folder numit “intrari” in care administratorii cladirii vor incarca fisierele generate de primul tip de porti. Programul va citi fiecare fisier din acel director, va incarca datele in baza de date, in tabela “access” si apoi va muta fisierul intr-un director numit backup_intrari. Numele fisierelor va avea formatul Poarta[numar_poarta].[tip_fisier] (de exemplu Poarta1.csv). Numele portii pe care se face fiecare intrare trebuie salvat in baza. Programul trebuie sa citeasca fisierul imediat ce acesta apare. (Verifica la fiecare iteratie daca exista fisiere noi in folderul intrari).
•	Al doilea tip de poarta: La nivelul programului, creati un endpoint care primeste ca parametru un json cu urmatorul format si il salveaza in baza de date: 
{
     "data":"2023-05-21T13:49:51.141Z",
     "sens":"in",
     "idPersoana":10,
     "idPoarta":3
}
•	Creati o functionalitate care sa ruleze zilnic, dupa ora 20:00, care sa calculeze numarul de ore lucrate de fiecare angajat, pe baza intrarilor si iesirilor inregistrate la porti. Pentru fiecare angajat care nu a lucrat 8 ore intr-o zi, un email va fi transmis catre managerul acestuia. De asemenea, lista cu numele angajatilor va fi scrisa si in directorul backup cu numele <data_curenta>_chiulangii.csv si <data_curenta>_chiulangii.txt si va contine angajatii in formatul Nume,OreLucrate atat in csv cat si in txt ( in txt nu va avea header) 
•	Adaugati orice functionalitate pe care o considerate interesanta sau utila. 

Hint: O persoana poate intra si iesi pe diferite porti. Toate intrarile si iesirile trebuie luate in calcul. 

Prerequisites: 

Trebuie sa aveti un fisier numit constants.py care sa contina informatiile bazei de date. 

Structura baza de date:
Acces: 
	-Id: int 
	-Id_Persoana: int 
	-Data: datetime/timestamp
	-Sens: varchar(3) ['in' sau 'out']
	-Poarta: int [contine numarul portii la care s-a facut inregistrarea] 

Persoane: 
	-Id: int 
	-Nume: Varchar(50) 
	-Prenume: Varchar(50)
	-Companie: Varchar(50)
	-IdManager: int 
	-Email: Varchar(50)

Puteti adauga coloane la tabelele mentionate insa acestea trebuie neaparat sa existe. 

Teste:
main.py 1 /cale/catre/fisier  
  -test 1.1
	  - se incarca un fisier txt Poarta1.txt
	  - se incarca un fisier csv Poarta2.csv 
	  - se verifica daca acestea sunt procesate iar inregistrarile sunt stocate in baza de date 
  -test 1.2
	  - se verifica daca au fost copiate fisierele in directorul backup si redenumite corect
  	  - se verifica daca fisierele au fost sterse din fisierul sursa 
main.py 2  
  -test 2.1
	  - se creeaza un request catre serverul pe care voi il veti crea
	  - se verifica in baza de date daca utilizatorul a fost creat corect 
  -test 2.2
      - se creeaza 10 requesturi catre server 
	  - se verifica daca datele au fost corect inregistrate in baza de date 
main.py 3 
  -test 3.1 
	  - se verifica daca angajatii care nu au lucrat suficient sunt calculati corect 
	  - se verifica daca