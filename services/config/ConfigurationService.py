from diagnostics.Severity import Severity
from diagnostics.TraceSources import TraceSources
from pymongo import MongoClient

TS = TraceSources.Get("ConfigurationService")

class ConfigurationService:
	def __init__(self):
		TS.TraceVerbose("Initializing ConfigurationService...")
		self.InitializeProperties()
		TS.TraceVerbose("Finished initializing ConfigurationService")
	
	def InitializeProperties(self):
		# TODO: Having a config file would be nice
		self.Properties = { }
		self.Properties["TraceLevel"] = Severity.Verbose

	def GetConfigProperty(self, name):
		if not (name in self.Properties):
			TS.TraceWarning("'{0}' configuration property not found".format(name))
			return None
		return self.Properties[name]
	
	def GetInstance():
		return service

service = ConfigurationService()