from .TraceSource import TraceSource
from .Severity import Severity

class TraceSources:
	traceLevel = Severity.Information
	traceSources = { }

	def SetTraceLevel(sev):
		TraceSources.traceLevel = sev

	def Get(name):
		if (name in TraceSources.traceSources):
			return TraceSources.traceSources[name]
		TraceSources.traceSources[name] = TraceSource(name, TraceSources.traceLevel)
		return TraceSources.traceSources[name]