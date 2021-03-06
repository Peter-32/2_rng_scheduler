from __future__ import print_function
from datetime import datetime, timedelta
import pickle
import random
import sys
from datetime import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main(days_to_schedule_out):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    event_types = [
    'Coursera courses and blog',
    'Data project and blog',
    'Data project and blog',        
    'Swift and blog',
    'Swift and blog',
    'Swift and blog',
    'Swift and blog',
    'Swift and blog',
    'Swift and blog',
    'Swift and blog',
    'Java/Kotlin and blog',
    'Java/Kotlin and blog',
    'Java/Kotlin and blog',
    'JavaScript and blog',
    'Serverless platforms like firebase, squarespace, email marketing services, video uploads, image uploads, chat services, payment services, api services like zapier.  Simpler the code base the better.',    
    'Serverless platforms like firebase, squarespace, email marketing services, video uploads, image uploads, chat services, payment services, api services like zapier.  Simpler the code base the better.',    
    'Serverless platforms like firebase, squarespace, email marketing services, video uploads, image uploads, chat services, payment services, api services like zapier.  Simpler the code base the better.',    
    'Social media like twitter, youtube, instagram, linkedin, facebook, tiktok, snapchat; navigate these platforms and promotion of apps and products',
    'Social media like twitter, youtube, instagram, linkedin, facebook, tiktok, snapchat; navigate these platforms and promotion of apps and products',
    'Social media like twitter, youtube, instagram, linkedin, facebook, tiktok, snapchat; navigate these platforms and promotion of apps and products',        
    'C# with unity game development',
    '6o9',
    ]

    now = datetime.now()
    for days_ahead in range(int(days_to_schedule_out)):
        is_sunday = False
        for slot in range(1,4):
            my_datetime = (now - timedelta(hours=7) + timedelta(days=days_ahead))
            if my_datetime.weekday() == 6:
                is_sunday = True
                continue
            date = my_datetime.strftime("%Y-%m-%d")
            if slot == 1:
                start_time = '17:30:00-07:00'
                end_time = '18:20:00-07:00'
            elif slot == 2:
                start_time = '20:00:00-07:00'
                end_time = '20:50:00-07:00'
            elif slot == 3:
                start_time = '21:00:00-07:00'
                end_time = '21:50:00-07:00'
            elif slot == 4:
                start_time = '13:00:00-07:00'
                end_time = '13:50:00-07:00'
            elif slot == 5:
                start_time = '14:00:00-07:00'
                end_time = '14:50:00-07:00'
            elif slot == 6:
                start_time = '15:00:00-07:00'
                end_time = '15:50:00-07:00'
            elif slot == 7:
                start_time = '16:00:00-07:00'
                end_time = '16:50:00-07:00'
            start_datetime = f'{date}T{start_time}'
            end_datetime = f'{date}T{end_time}'

            event = {
              'summary': random.choice(event_types),
              'start': {
                'dateTime': start_datetime,
                'timeZone': 'America/Los_Angeles',
              },
              'end': {
                'dateTime': end_datetime,
                'timeZone': 'America/Los_Angeles',
              },
            }
            event = service.events().insert(calendarId='primary', body=event).execute()
        if is_sunday:
            continue

    print("Done")

if __name__ == '__main__':

    main(sys.argv[1])
