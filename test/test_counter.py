# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock
from datetime import datetime

from counter import main, get_name, get_seasons, get_episodes

def mock_get_name(path):
    if path == 'test/testdrama':
        dt_str = datetime.now().strftime("%y%m%d%H%M%S")
        return 'testdrama' + dt_str
    else:
        return get_name(path)

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

        self.assertEqual(get_name('test/testdrama/01/02.txt'), '02')

    def test_get_seasons(self):
        self.assertEqual(get_seasons("test/testdrama"), ["test/testdrama/01", "test/testdrama/02"])

    def test_get_episodes(self):
        self.assertEqual(get_episodes("test/testdrama/01"), ["test/testdrama/01/01.txt", "test/testdrama/01/02.txt"])

    @patch('counter.get_name', mock_get_name)
    def test_main(self):
        main('test/testdrama')
