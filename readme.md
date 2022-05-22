# Global task

## My Approach

~~~
For this task, I have used Python Django Rest Framework. I have defined a Track model with attributes- title, artist, duration, and last_play. To load the JSON data to the database, I used BaseCommand class of django.core.management.base package. After loading the data to the database, I defined views and URLs according to what was asked in the task. I have defined a model viewset for the track model to get the list of tracks, retrieve a unique track, and post and update a track. I used Django-url-filter to provide a filter and ordering capabilities to the API for tasks 3 and task 4. For the Bonus task, I created an API with endpoint (artists/) and used SerializerMethodField in the serializer of this class to calculate the total_number_of_tracks, and most_recently_played_track for each artist.
~~~
## Loading of json data to database
Use the below command by replacing json_file_path with path of the json file to load the data to the database.

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
After running the application, detail about the apis are available as swagger documentation at url (http://127.0.0.1:8000
/swagger)

collection of postman request is saved as Global_tasks.postman_collection.json file in the folder and can be imported in postman for making requests through it. 

  
