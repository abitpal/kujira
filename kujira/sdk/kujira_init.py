'''
function to initialize the kujira set up: logs the user in and sets up a project configuration
'''
from kujira.sdk.kujira_run import Run

def init(
	job_type: str | None = None,
	project: str | None = None,
	analytics_file: str | None = None 
    ) -> Run:

	run = Run(analytics_file)
	return run



