from diagnostics.TraceSources import TraceSources

TS = TraceSources.Get("CommandService")

class CommandService:
	def __init__(self):
		TS.TraceVerbose("Initializing CommandService...")
		self.commandHandlers = { }
		TS.TraceVerbose("Finished initializing CommandService")

	def Register(self, symbol, handler):
		if (symbol in self.commandHandlers):
			TS.TraceWarning("'{0}' command already registered".format(symbol))
			return
		self.commandHandlers[symbol] = handler
	
	def Handle(self, message):
		if not "Symbol" in message:
			TS.TraceWarning("Message not properly formatted")
			return
		
		symbol = message["Symbol"]
		if not symbol in self.commandHandlers:
			TS.TraceWarning("No handler registered for '{0}'".format(symbol))
			return
		
		handler = self.commandHandlers[symbol]
		response = handler(message)
		return response

	def GetInstance():
		return service

service = CommandService()