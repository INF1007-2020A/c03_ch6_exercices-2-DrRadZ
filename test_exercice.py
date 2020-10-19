#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import randint
import sys
import unittest
from structs import Queue, Stack

import exercice


class TestExercice(unittest.TestCase):
    def test_reverse(self):
        values = ["a", "b", "z", "patate"]

        output = exercice.reverse_data(values)
        answer = ["patate", "z", "b", "a"]

        self.assertListEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_delete_stack(self):
        lifo = Stack()
        lifo.put_many(list(range(20)))
        
        answer = Stack()
        answer.put_many(list(range(19)))

        output = exercice.delete_nth_from_stack(lifo, len(lifo) - 1)

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_delete_queue(self):
        fifo = Queue()
        fifo.put_many(list(range(20)))
        
        answer = Queue()
        answer.put_many(list(range(1, 20)))

        output = exercice.delete_nth_from_queue(fifo, 0)

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_sort_stack(self):
        values = [randint(0, 1000) for _ in range(20)]
        lifo = Stack()
        lifo.put_many(values)

        output = exercice.sort_stack(lifo)
        answer = Stack()
        answer.put_many(sorted(values))

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_sort_queue(self):
        values = [randint(0, 1000) for _ in range(20)]
        fifo = Queue()
        fifo.put_many(values)

        output = exercice.sort_stack(fifo)
        answer = Queue()
        answer.put_many(sorted(values))

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_string_and_structs(self):
        sequence = "te!eYy.E6e/T"

        output_fifo, output_lifo = exercice.string_and_structs(sequence)
        fifo, lifo =  Queue, Stack
        fifo.put_many("Yeet")
        lifo.put_many("yEeT")

        self.assertEqual(
            output_fifo,
            fifo,
            'Mauvaise reponse'
        )

        self.assertEqual(
            output_lifo,
            lifo,
            'Mauvaise reponse'
        )

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)