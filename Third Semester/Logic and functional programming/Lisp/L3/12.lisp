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
