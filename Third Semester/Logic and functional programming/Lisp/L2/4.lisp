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



