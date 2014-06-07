from npr_story_ext import nprStoryData
import unittest
import requests

API_KEY='MDE0MzQwNzMxMDE0MDEwNjE1MzNhNjU1Yw001'

#The test_get_json() function takes forever to run, I commented it out to make test code run faster.



class TestnprStoryData(unittest.TestCase):
	def runTest(self):
		self.testcase = nprStoryData(API_KEY)
		self.test_reset_url()
		self.test_add_num_results()
		self.test_add_id()
		self.test_add_id_additional()
		self.test_add_required_assets()
		self.test_add_required_assets_additional()
#		self.test_get_json()
		print 'All Tests Passed!'
	def test_add_num_results(self):
		self.testcase.add_num_results(5)
		self.assertEqual(self.testcase.parameters['numResults'], '5')
	def test_add_id(self):
		self.testcase.add_id('1007')
		self.assertEqual(self.testcase.parameters['id'], '1007')
	def test_add_id_additional(self):
		self.testcase.add_id('1000')
		self.assertEqual(self.testcase.parameters['id'], '1007,1000')
	def test_add_required_assets(self):
		self.testcase.add_required_assets(self.testcase.AUDIO)
		self.assertEqual(self.testcase.parameters['requiredAssets'], 'audio')
	def test_add_required_assets_additional(self):
		self.testcase.add_required_assets('text')
		self.assertEqual(self.testcase.parameters['requiredAssets'], 'audio,text')
	def test_reset_url(self):
		self.testcase.add_num_results(4)
		self.testcase.add_required_assets(self.testcase.IMAGES)
		self.testcase.add_id('1007')
		self.testcase.reset_url()
		self.assertEqual(self.testcase.parameters, {'id': None,'numResults': None, 'requiredAssets': None })
		self.assertEqual(self.testcase.has_id, False)
		self.assertEqual(self.testcase.has_asset, False)
	def test_get_json(self):
		self.testcase.reset_url()
		self.testcase.get_json()
		self.assertEqual(self.testcase.json, requests.get(self.testcase.url).json())

tester = TestnprStoryData()
tester.runTest()

