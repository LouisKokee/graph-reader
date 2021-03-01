from unittest import TestCase
from functions import *


class Test(TestCase):
    def test_pix_list_to_graph_data(self):
        result = pixList_to_graphData([100], 50, 500)
        self.assertEqual(result, 10)