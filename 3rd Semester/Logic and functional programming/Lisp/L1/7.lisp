 ; a) Sa se scrie o functie care testeaza daca o lista este liniara.
;; test_liniara(l1...ln) = true, n = 0
;;                         nil, l1 - lista
;;                         test_liniara(l2...ln), altfel
(defun test-liniara (lst)
  (cond
    ((null lst) t)
    ((listp (car lst)) nil)
    (t (test-liniara (cdr lst)))
    )
  )

;( b) Definiti o functie care substituie prima aparitie a unui element intr-o lista data.
;; 
;; substituieElement(eV, eN, l1...ln) = nil, n = 0
;;                                      substituieElement(eV, eN, l1) + (l2...ln), l1 - lista si existaInLista(eV, l1)
;;                                      (eN) + (l2...ln), l1 - atom si eV = l1
;;                                      l1 + substituieElement(eV, eN, l2...ln), altfel
(DEFUN substituieElement (eV eN l)
  (COND
    ((null l)                                           nil)
    ((AND (listp (CAR l)) (existaInLista eV (CAR l)))   (CONS (substituieElement eV eN (CAR l)) (CDR l)))
    ((AND (atom (CAR l)) (equal (CAR l) eV))            (CONS eN (CDR l)))
    (T                                                  (CONS (CAR l) (substituieElement eV eN (CDR l))))
    )
  )

;; existaInlista(eV, l1...ln) = nil, n = 0
;;                              existaInlista(eV, l1) sau existaInLista(eV, l2...ln), l1 - lista
;;                              true, eV = l1
;;                              existaInLista(eV, l2...ln), altfel
(DEFUN existaInLista (eV l)
  (COND
    ((null l)             nil)
    ((listp (CAR l))      (OR (existaInLista eV (CAR l)) (existaInLista eV (CDR l))))
    ((equal (CAR l) eV)   T)
    (T                    (existaInLista eV (CDR l)))
    )
  )

; c) Sa se inlocuiasca fiecare sublista a unei liste cu ultimul ei element. 
;Prin sublista se intelege element de pe primul nivel, care este lista. 
;Exemplu: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==> (a c (f)) ==> (a c f)
;         (a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f)

;; inverseaza(l1 ... ln) = nil                           , daca n = 0
;;                         inverseaza(l2 ... ln) (+) (l1), altfel
(DEFUN inverseaza(l)
  (COND
    ((null l) nil)
    (T        (APPEND (inverseaza (CDR l)) (list (CAR l))))
    )
  )

;; lastElement(l1 ... ln) = lastElement(p1), daca l - lista, (unde p1 ... pn = inverseaza(l))
;;                          l              , altfel
(DEFUN lastElement (l)
  (if (listp l) 
      (lastElement (CAR (inverseaza l)))
      l
      )
  )

;; inlocuiesteSubliste(l1 ... ln) = nil                                               , daca n = 0
;;                                  lastElement(l1) (+) inlocuiesteSubliste(l2 ... ln), daca l1 - lista
;;                                  {l1} (+) inlocuiesteSubliste(l2 ... ln)           , altfel
(DEFUN inlocuiesteSubliste (l)
  (COND
    ((null l)   nil)
    ((listp (car l))  (CONS (lastElement (CAR l)) (inlocuiesteSubliste (CDR l))))
    (T          (CONS (CAR l) (inlocuiesteSubliste (CDR l))))
    )
  )


; d) Definiti o functie care interclaseaza fara pastrarea dublurilor doua liste liniare sortate.

;; interclasare( l1...ln, p1...pm) = l1...ln , m =0
;;                                   p1...pm, n = 0
;;                                   l1 + interclasare(l2...ln, p1...pm), daca l1 < p1
;;                                   p1 + interclasare(l1...ln, p2...pm), daca p1< l1
;;                                   l1 + interclasare(l2...ln, p2...pm), daca l1 = p1
(defun interclasare (l1 l2)
  (cond
    ((null l2) l1)
    ((null l1) l2)
    ((< (car l1) (car l2)) (cons (car l1) (interclasare (cdr l1) l2)))
    ((> (car l1) (car l2)) (cons (car l2) (interclasare l1 (cdr l2))))
    (t (cons (car l1) (interclasare (cdr l1) (cdr l2))))
    ))
