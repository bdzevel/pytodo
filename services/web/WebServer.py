from flask import Flask
from flask import request
from diagnostics.TraceSources import TraceSources
from services.command.CommandService import CommandService

TS = TraceSources.Get("WebServer")

class WebServer(Flask):
	def __init__(self):
		TS.TraceVerbose("Initializing WebServer...")
		super(WebServer, self).__init__("pytodo")
		self.commandService = CommandService.GetInstance()
		self.initializeRoutes()
		TS.TraceVerbose("Finished initializing WebServer")

	def initializeRoutes(self):
		@self.route("/", methods=["GET"])
		def index():
			return "Hello, INDEX!"

		@self.route("/api/command", methods=["POST"])
		def apiCommand():
			message = request.get_json()
			resp = self.commandService.Handle(message)
			return resp, 200, None
	
	def GetInstance():
		return webServer

webServer = WebServer()