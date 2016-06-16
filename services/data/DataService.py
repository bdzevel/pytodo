from services.config.ConfigurationService import ConfigurationService
from diagnostics.TraceSources import TraceSources
from pymongo import MongoClient

TS = TraceSources.Get("DataService")

class DataService:
	def __init__(self):
		TS.TraceVerbose("Initializing DataService...")
		self.InitializeServices()
		self.InitializeDBClient()
		TS.TraceVerbose("Finished initializing DataService")

	def InitializeServices(self):
		self.ConfigurationService = ConfigurationService.GetInstance()

	def InitializeDBClient(self):
		mongoURL = self.ConfigurationService.GetConfigProperty("MongoURL")
		self.Client = MongoClient(mongoURL)
		self.Database = self.Client["pytodo"]

	def Select(self, collectionName, **conditions):
		return self.Database[collectionName].find(conditions)

	def SelectOne(self, collectionName, **conditions):
		return self.Database[collectionName].find_one(conditions)

	def Insert(self, collectionName, item):
		return self.Database[collectionName].insert_one(item)
		
	def Delete(self, collectionName, item):
		self.Database[collectionName].delete_one(item)
	
	def GetInstance():
		return service

service = DataService()