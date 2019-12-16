import unittest
import englishnumber

class TestEnglishNumber(unittest.TestCase) :
    def test_numbers(self) :
      numbers = [ (0.01, "None and 01/100"),
                    (1.25, "One and 25/100"),
                    (12.34, "Twelve and 34/100"),
                    (119.12, "One Hundred Nineteen and 12/100"),
                    (1001.34, "One Thousand One and 34/100"),
                    (1211.45, "One Thousand Two Hundred Eleven and 45/100"),
                    (1234567.68, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven and 68/100"),]

      en = englishnumber.EnglishNumber()
      for n in numbers:
        nstr = "{:0.2f}".format(n[0])
        en.SetNumber(nstr)
        self.assertEqual(n[1],en.GetNumber())


if __name__=="__main__":
    unittest.main()
