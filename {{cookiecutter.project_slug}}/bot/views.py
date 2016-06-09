from django.http import HttpResponse

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *

# Create your views here.


class SMSView(APIView):
	"""
	Accept POST requests from Twilio's server for SMS and eventually MMS.
	"""
	def post(self, request, format=None):
		"""
		Twilio posts here and expects a 200 in return. Reply messages + delivery are handled async.
		TODO: adapt the post method below to follow the SendMessageView at the bottom of this file.
		And you still have to settle the question of where reply sending happens - especially w/ scheduling messages.
		"""
		# get the body of the request
		msg_dict = request.data
		if msg_dict is None:
			# there was no message body
			return Response(status=status.HTTP_400_BAD_REQUEST)

		# try to get the user profile

		# deserialize and create the message object
		# well, we're just gonna create it straight from the dict
		try:
			message_body = msg_dict['Body']

			# check for empty body
			if message_body == u'':
				# reply = "Did you send a pic or something? I can only see text."
				# send_messages(reply, profile)
				return Response(status=status.HTTP_200_OK)
			else:
				# save the user's message to us.
				pass
		except KeyError:
			# non-existent body
			# reply = "Did you send a pic or something? I couldn't understand your text."
			# send_messages(reply, profile)
			return Response(status=status.HTTP_200_OK)

		# if there's a message, then we make a reply

		return Response(status=status.HTTP_200_OK)


