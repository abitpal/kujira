'''
function to initialize the kujira set up: logs the user in and sets up a project configuration
'''
from kujira.sdk.kujira_run import Run

def init(
	analytics_file: str | None = None,
	job_type: str | None = None,
	project: str | None = None,
    ) -> Run:

	run = Run(analytics_file) #just returns the Run 
	return run



