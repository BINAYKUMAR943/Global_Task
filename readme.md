# Global task


## Steps I followed
For these tasks, I have used Python Django Rest Framework. I have defined a Track model with attributes- title, artist, duration, and last_play. I have lodaded the json data to the model using BaseCommand class of django.core.management.base package. I have defined a model viewset for the track model to get the list of tracks, retrieve a unique track, and post and update a track. And have used Django-url-filter in this project to provide filtering and ordering capabilities to the APIs for tasks 3 and task 4.

For task 3, to get the list of hundred most recent track, pass the parameter- limit=100 and ordering=-last_play (example- http://127.0.0.1:8000/tracks/?limit=100&ordering=-last_play)
Note: On Running you will get two extra tracks added by me for testing.

For task 4, to filter track by name, pass the parameter- ?title=titlename (example-http://127.0.0.1:8000/tracks/?title=Free)

 For the Bonus task, I have created an API with endpoint (artists/) and used SerializerMethodField in the serializer of this class to calculate the total_number_of_tracks, and most_recently_played_track for each artist.

## Loading of json data to database

I have used the below command to load the json data to the database. Note: You don't need to run this command again as data has already been loaded to the database.

 ```
 python manage.py mycommand json_file_path

 ```


## Setting up the envrionment
Create a virtual environment, install all the required packages mentioned in the requirements.txt file

```

virtualenv .venv
pip3 install -r requirements.txt

```

## Running the application


To start the development server, you just need to run: 

```
python manage.py runserver

```

This will start the development server running on port 8000. 


## Documentation
After running the application, detail about the apis are available as swagger documentation at url (http://127.0.0.1:8000/swagger)

collection of postman request is saved as Global_tasks.postman_collection.json file in the folder and can be imported in postman for making requests through postman. 

  
