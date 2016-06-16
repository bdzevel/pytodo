from diagnostics.Severity import Severity
from diagnostics.TraceSources import TraceSources
from services.web.WebServer import WebServer
from services.config.ConfigurationService import ConfigurationService

# SET TRACE LEVEL
configService = ConfigurationService.GetInstance()
TraceSources.SetTraceLevel(configService.GetConfigProperty("TraceLevel"))

# BOOTSTRAP FLASK
webServer = WebServer.GetInstance()