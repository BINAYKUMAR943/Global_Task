# Global task

## My Approach

~~~
1) I created a model named Track with attributes- title,artist,duration,last_play and migrated the same to the database.
2) Loaded the json data to the database. For this purpose, I extended BaseCommand class of django.core.management.base package and overriden add_arguments, handle methods.
3) Defined views and urls according to what was asked in the task. 
    i I defined a model viewset for track model to get the list of tracks, to retreive a unique track, to post and update a track.
    ii I used django-url-filter to provide filter and ordering capabilties to the api for task 3 and task 4.
    iii For Bonus task, I created an api with endpoint (artists/) and used SerializerMethodField in the serializer of this class to calculate the total_number_of_tracks, and most_recently_played_track for each artist.
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

  
