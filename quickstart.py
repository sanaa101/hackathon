from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#If modifying these scopes, delete the file token.picle
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    "Shows basic usage of Google Calendar API. "
    "Prints the start and name of the next 10 events on the user."
    
    creds = None
    #The file token.picle stores the user's access and refresh tokens, and is
    #created automatically when the authorization flow completes for the first
    #timeA
    if os.path.exists('token pickle'):
        with open('token.picke', 'rb') as token:
            creds = pickle.load (token)
    #If there are no valid credentials availible, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        #save the credentials for the next run
        with open('token.pickle','wb') as token:
            pickle.dump(creds,token)
    service = build('calendar', 'v3' , credentials=creds)

    #Call the Calandar API
    now=datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' idicates UTC time
    print('Getting the upcoming 10 events')
    event_reselt = service.events().list(calendarId='primary', timeMin=now, maxResults=10,singleEvents=True,orderBy='startTime').execute()
    events = events_reseult.get('item', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = events['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()