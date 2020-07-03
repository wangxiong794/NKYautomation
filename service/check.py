import unittest


class Check(unittest.TestCase):
    def check(self, hope, text):
        if isinstance(hope, dict):
            for key in hope.keys():
                if isinstance(hope[key], list):
                    for v in hope[key]:
                        self.assertIn(v, text[key])
                else:
                    self.assertEqual(hope[key], text[key])
        elif isinstance(hope, str):
            self.assertIn(hope, str(text))

    def check_bill(self, hope, text):
        if hope == "单据号":
            pass
        else:
            if isinstance(hope, dict):
                for key in hope.keys():
                    if isinstance(hope[key], list):
                        for v in hope[key]:
                            self.assertIn(v, text[key])
                    else:
                        self.assertEqual(hope[key], text[key])
            elif isinstance(hope, str):
                self.assertIn(hope, str(text))