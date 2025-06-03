# test_module.py
import unittest
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for testing

from medical_data_visualizer import draw_cat_plot, draw_heat_map

class DataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig, "draw_cat_plot() returned None")
        self.assertEqual(fig.axes[0].get_title(), "", "Cat plot should not have a title by default")
        self.assertEqual(len(fig.axes[0].patches), 35, "Unexpected number of bars in catplot")

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig, "draw_heat_map() returned None")
        self.assertEqual(fig.axes[0].get_title(), "", "Heatmap should not have a title by default")
        self.assertEqual(len(fig.axes[0].collections), 1, "Heatmap should have one main collection")

if __name__ == "__main__":
    unittest.main()
