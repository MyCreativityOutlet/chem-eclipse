import unittest


class TestImporting(unittest.TestCase):

    def test_importing_self(self):
        from eclipse.utils import prepare_envipath_data
        from eclipse.eclipseTrain import eclipse_train_main
        from eclipse.eclipseInference import eclipse_inference_main, oob_inference
        from eclipse.ProductPredictionTrain import product_main
        from eclipse.ModelAnalysis import recreate_tables_figures
