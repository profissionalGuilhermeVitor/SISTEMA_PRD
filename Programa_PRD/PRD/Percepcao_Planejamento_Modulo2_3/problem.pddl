(define (problem problemPDDL)
    (:domain blocks-domain)
    (:requirements :disjunctive-preconditions :equality :negative-preconditions :strips :typing)
    (:objects a b c d e t1 t2 t3 t4 t5 - block)
    (:init (clear a) (clear b) (clear c) (clear d) (clear t4) (emptyhand) (on a e) (on b t5) (on c t3) (on d t2) (on e t1) (table t1) (table t2) (table t3) (table t4) (table t5))
    (:goal (and (on e t5) (on a e) (on d t3) (on c b) (on b d)))
)