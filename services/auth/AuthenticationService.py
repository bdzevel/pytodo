import bcrypt
from constants.auth import constants
from diagnostics.TraceSources import TraceSources
from services.data.DataService import DataService
from services.command.CommandService import CommandService

TS = TraceSources.Get("AuthenticationService")
messages = constants["Messages"]

class AuthenticationService:
	def __init__(self):
		TS.TraceVerbose("Initializing AuthenticationService...")
		self.InitializeServices()
		self.RegisterHandlers()
		TS.TraceVerbose("Finished initializing AuthenticationService")

	def InitializeServices(self):
		self.dataService = DataService.GetInstance()
		self.commandService = CommandService.GetInstance()

	def RegisterHandlers(self):
		self.commandService.Register(messages["Register"], self.RegisterUser)
		self.commandService.Register(messages["Authenticate"], self.Authenticate)

	def RegisterUser(self, message):
		username = message["Parameters"]["UserName"]
		password = message["Parameters"]["Password"]
		
		if (self.dataService.Select("Users", { "UserName": username }).count() != 0):
			return { "Symbol": messages["RegisterResponse"], "Parameters": { "Result": -1, "Error": "User already exists" } }

		salt = bcrypt.gensalt()
		hash = bcrypt.hashpw(password, salt)
		result = self.dataService.Insert("Users", { "UserName": username, "PasswordHash": hash })
		return { "Symbol": messages["RegisterResponse"], "Parameters": { "Result": 0, "Token": result.inserted_id } }

	def ValidateToken(self, token):
		user = self.DataService.SelectOne("Users", { "_id": token })
		if (user):
			return True
		return False

	def Authenticate(self, message):
		username = message["Parameters"]["UserName"]
		password = message["Parameters"]["Password"]
		
		users = self.dataService.Select("Users")
		user = self.findUser(users, username)
		if (user and bcrypt.hashpw(password, user["PasswordHash"]) == hash):
			return { "Symbol": messages["AuthenticateResponse"], "Parameters": { "Result": 0, "Token": user["_id"] } }
		return { "Symbol": messages["AuthenticateResponse"], "Parameters": { "Result": -1, "Error": "Invalid username/password" } }

	def findUser(self, users, username):
		for user in users:
			if (user.UserName == username):
				return user
		return None

	def GetInstance():
		return service

service = AuthenticationService()