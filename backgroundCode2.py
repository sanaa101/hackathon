#This code is called by the flask code, and contains the function go() which checks two users google calendar information to see if there  are any conlflicts
#Currently, this program only checks the next 10 events of 2 users and checks to see if there is a conflict with a predetermined time
#Note: this is a development version of this code to be used independently from the flask code for testing purposes


from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
count = 0

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def go():
    count = 0
    while (count<2):
        count = count + 1
        #Currently this prints the start and name of the next 10 events on the user
    
        creds = None
        #timeA
        if count==1:
           # if not creds or not creds.valid:
           #     if creds and creds.expired and creds.refresh_token:
           #         creds.refresh(Request())
           #     else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            service = build('calendar', 'v3' , credentials=creds)

        #timeB
        if count==2:
        #If there are no valid credentials availible, let the user log in.
        #    if not creds or not creds.valid:
        #        if creds and creds.expired and creds.refresh_token:
        #            creds.refresh(Request())
        #        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

            service = build('calendar', 'v3' , credentials=creds)
        #Call the Calendar API
        now=datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' idicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary',timeMin = now, maxResults=10,singleEvents=True,orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            print(event['start'].get('dateTime'), event['summary'])
            #below is a test to see if the current event conflits with a predetermined time. In future will store this information into a list to see if 2 schedules conflict
            if(event['start'].get('dateTime') == '2020-09-14T14:00:00-05:00'):
                print('there is a conflict')

if __name__ == '__main__':
    go()
