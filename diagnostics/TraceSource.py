from .Severity import Severity

class TraceSource:
	def __init__(self, name, severity):
		self.Name = name
		self.TraceLevel = severity
	
	def Trace(self, severity, message):
		if (severity.value <= self.TraceLevel.value):
			print(FormatMessage(self.Name, message))
	
	def TraceError(self, message):
		self.Trace(Severity.Error, message)
	
	def TraceWarning(self, message):
		self.Trace(Severity.Warning, message)
	
	def TraceInformation(self, message):
		self.Trace(Severity.Information, message)
	
	def TraceVerbose(self, message):
		self.Trace(Severity.Verbose, message)

def FormatMessage(traceName, message):
	return "[{0}] {1}".format(traceName, message)