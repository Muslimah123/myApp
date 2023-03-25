# myApp
The whole project is about building a voice enabled financial management system for smaller businesses
In this example, we've added a new function called create_voice_transcripts_table which creates a new table called "voice_transcripts" with columns for the ID of the user who recorded the voice, the actual transcript text, and the date the transcript was created.

We've also added a new function called store_voice_transcript which takes in the user ID and transcript text as arguments and inserts them into the "voice_transcripts" table.

Finally, we've added a new route called "/store-voice-data" which handles requests to store new voice transcript data. This route expects the transcript text to be included in the request as a form field called "voice_transcript". When a request is received, the route gets the user ID from the session (assuming the user is logged in), stores the voice transcript in the database using the store_voice_transcript function, and returns a success response to the client.

# Prerequisites
- Apache XAMMP running

# Setup project

#  1. Create virtual environment
```bash
python -m venv myenv
```

# 2 . Activate virtual environment
```bash
source myenv/Script/activate
```
# 3 . Install packages
```bash
pip install -r requirements.txt

```
# 4. Run the app
```bash
flask run 
```

# 5. Visit the app in the url
```bash
localhost:5000
```


### Note
Always do `pip freeze > requirements.txt` after installing new packages

```bash
git checkout -b feat/idaya
```


```bash
git checkout -b feat/sam

```
## Add your changes 

```bash 
git add .
git commit -m "update feat/idaya"
git push origin feat/idaya
```


```bash 
git add .
git commit -m "update feat/sam"
git push origin feat/sam
```