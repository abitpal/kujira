import os
import traceback
import importlib
import sys
import time

class Run:
	def __init__(self, analytics_file):
		self.analytics_file = analytics_file
		sys.path.append(analytics_file)
		self.prev_edit = self._get_time()
		self._get_analytics()

	def _get_analytics(self): 
		spec = importlib.util.spec_from_file_location('analytics', self.analytics_file)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		self.analytics = module.collect

	def _update_analytics(self) -> bool:
		if (self._get_time() != self.prev_edit):
			self.prev_edit = self._get_time()
			self._get_analytics()
		
	def _get_time(self):
		return os.stat(self.analytics_file).st_ctime
	
	def __call__(self, *args, **kwargs):
		self._update_analytics()

		try: 
			self.analytics(*args, **kwargs)
		except exception:
			print("Error Encountered -- Sleeping for 0.5 seconds before retrying...")
			print(traceback.format_exc())
			time.sleep(0.5)
			self.__call__(*args, **kwargs)




