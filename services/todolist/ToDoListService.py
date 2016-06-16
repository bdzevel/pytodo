from diagnostics.TraceSources import TraceSources
from pymongo import MongoClient

TS = TraceSources.Get("ToDoListService")

class ToDoListService:
	def __init__(self):
		TS.TraceVerbose("Initializing ToDoListService...")
		self.RegisterHandlers()
		TS.TraceVerbose("Finished initializing ToDoListService")

	def RegisterHandlers(self):
		pass

	def GetListItems(self):
		pass

	def GetInstance():
		return todoListService

todoListService = ToDoListService()