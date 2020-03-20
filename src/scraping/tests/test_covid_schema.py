# -*- coding: utf-8 -*-
"""temp-test-covid-qa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1415IFde2JEH52dzC7m4gbjTm6gC1D6fW
"""

#!wget --output-document=CDC_v0.1.json https://raw.githubusercontent.com/jsedoc/Covid-19-infobot/master/data/CDC_v0.1.json?token=ABNSURVRQXYT6XI2K5HAMJC6PUOCM
import unittest
import json, pprint

class TestDataSchemaJSON(unittest.TestCase):

    def test_load_json(self):
        self.cdc_data = json.load(open('../data/CDC_v0.1.json' , 'r'))

    def test_fielfs_exist(self):
        self.cdc_data = json.load(open('../data/CDC_v0.1.json' , 'r'))
        entry0 = self.cdc_data[0]
        assert 'topic' in entry0
        assert 'sourceUrl' in entry0
        assert 'typeOfInfo' in entry0
        assert 'questionText' in entry0
        assert 'answerText' in entry0
        assert 'isAnnotated' in entry0
        assert 'questionID' in entry0
        assert 'answerID' in entry0
        assert 'hasAnswer' in entry0
        assert 'containsURLs' in entry0
        assert 'needsUpdate' in entry0
        assert 'targetEducationLevel' in entry0

    def test_pprint(self):
        self.cdc_data = json.load(open('../data/CDC_v0.1.json' , 'r'))
        pprint.pprint(self.cdc_data)

if __name__ == '__main__':
    unittest.main()
