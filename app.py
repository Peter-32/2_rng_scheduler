from __future__ import print_function
from datetime import datetime, timedelta
import pickle
import random
from datetime import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
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
    event_types = ['My own courses on my blog website.',
    'Finish and post the Google project',
    'Introduction to probability models and PQRS(post)T',
    'Listen to nlp book PQRS(post)T',
    'Chess GM Videos',
    'Beat GW1 Completionist Swapping Roles RNG',
    'Beat BG2 Swapping Roles',
    'Play Chess and fill out 1000 lines in the "candidate moves1" file',
    'Relax',
    'All of the social graph book PQRS(post)T',
    'How to prove it PQRS(post)T',
    "silver pickaxe (Job / Work)",
    "shirt (Clothes)",
    "newspaper (News)",
    "silver map (Not too distant future)",
    "music notes (Music)",
    "video camera (Movies)",
    "book (Books)",
    "chess, programming, games (Hobbies)",
    "baby (Children)",
    "🐕 (Pets)",
    "arrow up to right (Current trends)",
    "laughing masks (Comedy / Humor)",
    "book with lightbulb (Learning / Studies)",
    "3x3 grid of dots (Apps)",
    "sphere with www (Internet)",
    "PS4 controller (Games)",
    "VR headset (Virtual reality)",
    "mobile phone (Phones)",
    "shield with a lock on it (Privacy)",
    "car with sensors (Self-driving cars)",
    "microphone with headphones (Podcasts)",
    "small plant growing (Where they grew up)",
    "kids throwing a ball (Things they were into)",
    "🏫 (School)",
    "3 people with arms around each other (Friends)",
    "parents with children (Family)",
    "bronze pickaxe (Previous jobs)",
    "bronze 🏠 (Where they have lived)",
    "bronze trophy (Accomplishments)",
    "green club (Clubs)",
    "cybertruck (Cars)",
    "christmas tree (Holidays)",
    "small printed photo (Photography)",
    "beach (The beach)",
    "hiking poles (Hiking)",
    "👽 (Aliens)",
    "arrows in a circle (Change)",
    "🌟 (Talents and Skills)",
    "dots around word habit (Habits)",
    "target (Goals)",
    "hand holding ❤️ (Charity / Volunteering)",
    "heart on a laptop (Online dating)",
    "lightning above person's head '(Stress)'},",
    "💡 with a brain inside (Creativity)",
    "superman icon (Heroes)",
    "smiling face (Happiness)",
    "Google AdWords (Marketing)",
    "🌟 with name Tom Cruise (Celebrities)",
    "Paper with 401k at the top (Retirement)",
    "male and female symbols (Stereotypes)",
    "💰 dropped in hands (Corruption)",
    "Cloud (Weather)",
    "gold map (The distant future)",
    "car (Driving)",
    "tree near bench (Parks / National Parks)",
    "rocketship (Space)",
    "cat (Animals)",
    "weight (Exercise / Being active)",
    "beer (Drinking)",
    "Google (Googling)",
    "Tent (Camping)",
    "Ice cream cone (Ice cream)",
    "Dress (Fashion)",
    "Four leaf clover (Luck)",
    "Bed (Sleep)",
    "Two wrenches (Fixing things)",
    "canvas and paintbrush (Art)",
    "Playing cards (Cards)",
    "Tree (Nature)",
    "Swimming (Swimming)",
    "i icon (Facts)",
    "thumbs down (Pet peeves)",
    "Violin (Musical instruments)",
    "History channel H (History)",
    "Hackerrank questions",
    "Program an AGI using looping AI programs itself",
    "Memorize the topics of conversation",
    "To know public speaking",
    "To know psychology",
    "To know business writing",
    "To know accounting",
    "To know design",
    "To know conversations",
    "To overcome shyness",
    "To know a second language",
    "To know about golfing",
    "To use proper grammar",
    "To know persuasion",
    "To know technology",
    "To use proper voice technique",
    "To imagine an incredible future",
    "To work towards a flexible schedule",
    "To do things I can steadily improve at",
    "To help others once I've helped myself",
    ]

    event_types = ['#1 Goal',
    'My book',
    'Guitar',
    'Drawing',
    ]


    now = datetime.now()
    days_to_schedule_out = 3
    for days_ahead in range(days_to_schedule_out):
        for slot in range(1,4):
            date = (now - timedelta(hours=7) + timedelta(days=days_ahead)).strftime("%Y-%m-%d")
            if slot == 1:
                start_time = '17:30:00-07:00'
                end_time = '18:20:00-07:00'
            elif slot == 2:
                start_time = '20:00:00-07:00'
                end_time = '20:50:00-07:00'
            else:
                start_time = '21:00:00-07:00'
                end_time = '21:50:00-07:00'
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


    print("Done")

if __name__ == '__main__':
    main()
