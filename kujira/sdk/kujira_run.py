import os
import traceback
import importlib
import sys
from colorama import Fore, Style


class Run:
	def __init__(self, analytics_file):
		self.analytics_file = analytics_file 
		sys.path.append(analytics_file)  #needed for importing the programs in the analytics file
		self.prev_edit = self._get_time()  #get the time of last edit 
		self._get_analytics()
		self.logs = {}

	def _get_analytics(self): 
		spec = importlib.util.spec_from_file_location('analytics', self.analytics_file) 
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		self.analytics = module.collect #.collect method is what Run will call

	def _update_analytics(self, forced = False) -> bool:
		if (self._get_time() != self.prev_edit or forced): #only re-import the analytics program if it has been edited
			self.prev_edit = self._get_time()
			self._get_analytics()
	
	#returns the time of last edit
	def _get_time(self):
		return os.stat(self.analytics_file).st_ctime
	
	def get_logged(self):
		pass
	
	def __call__(self, *args, **kwargs):
		
		forced = False

		while True: 
			try:  #runs the arguments on the analytics code
				self._update_analytics(forced)
				logs = self.analytics(*args, **kwargs)
				break
			except Exception: #if there's an error, we stop the program and let the user fix
				print('---------------------------------\n\n' + Fore.RED + traceback.format_exc())
				prev_exception = Exception
				print(Style.RESET_ALL + '---------------------------------\n')

				retry = input(Fore.BLUE + "Click 'Enter' to re-try the program: " + Style.RESET_ALL)
				print('\n')
				forced = True 



