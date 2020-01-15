# -*- coding: utf-8 -*-
from unittest import TestCase

from counter import main, get_name

class CounterTest(TestCase):

    def test_get_name(self):
        name = "drama"
        path1 = "drama"
        path2 = "drama/"
        path3 = "xx/drama"
        path4 = "aa/drama/"
        path5 = "~/drama"
        path6 = "~/drama/"
        path7 = "~/yy/drama"
        path8 = "~/bb/drama/"
        path9 = "/the/drama"
        path10 = "/foo/drama/"

        self.assertEqual(get_name(path1), name)
        self.assertEqual(get_name(path2), name)
        self.assertEqual(get_name(path3), name)
        self.assertEqual(get_name(path4), name)
        self.assertEqual(get_name(path5), name)
        self.assertEqual(get_name(path6), name)
        self.assertEqual(get_name(path7), name)
        self.assertEqual(get_name(path8), name)
        self.assertEqual(get_name(path9), name)
        self.assertEqual(get_name(path10), name)
