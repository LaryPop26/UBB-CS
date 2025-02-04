;; Sa se converteasca un arbore de tipul 2 in unul de tipul 1.
;; transformare (l1 ... ln) = nil, n = 0
;;                            [l1,0], n = 1
;;                            [l1,1] + transformare(l2), n = 2
;;                            [l1,2] + transformare(l2) + transformare(l3), n = 3
;;

(defun transformare (l)
  (cond
    ((null l ) nil)
    ((null (cadr l)) (append (list (car l)) (list 0)))
    ((null (caddr l)) (append (list (car l)) (list 1) (transformare (cadr l))))
    (t (append (list (car l)) (list 2) (transformare (cadr l)) (transformare (caddr l))))
  )
)

(print (transformare '(A (B) (C (D) (E)))))

(print (transformare '(A (B (D) (E (F (G) (H)))) (C (I (J (K)))))))

(print (transformare '(A (B (D (G)) (E (H (L (M) (N))) (I))) (C (F (J) (K (Q (P (R) (S)))))))))


;;  Definiti o functie care inlocuieste un nod cu altul intr-un arbore n-ar reprezentat sub forma (radacina lista_noduri_subarb1...lista_noduri_subarbn)  
;;  Ex: arborelele este (a (b (c)) (d) (e (f)))  si nodul 'b se inlocuieste cu nodul 'g => arborele (a (g (c)) (d) (e (f)))

;; substituire (x, e , s) = x, x- atom, x != e
;;                          s, x- atom, x = e
;;                          U(i=1) (n) substituire(xi,e,s), x - lista, x = x1x2...xn

(defun substituire(x e s)
  (cond
    ((and (atom x) (equal x e)) s)
    ((atom x) x)
    (t (mapcar #'(lambda (x) (substituire x e s)) x))
    )
  )

(print (substituire '(a (b (c)) (d) (e (f))) 'b 'g))

(print (substituire '(A (B (D (G)) (E (H (L (M) (N))) (I))) (C (F (J) (K (Q (P (R) (S))))))) 'E 'X))

(print (substituire '(a (b (c)) (d) (e (f))) 'x 'g))


