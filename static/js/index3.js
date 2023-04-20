// Request permission to access user's audio device
navigator.mediaDevices.getUserMedia({ audio: true })
  // If permission is granted, call the handlerFunction and pass it the audio stream
  .then(stream => {handlerFunction(stream)});

// Define the handlerFunction to handle the audio stream
function handlerFunction(stream) {
  // Create a MediaRecorder object to record audio from the stream
  rec = new MediaRecorder(stream);
  // When the MediaRecorder has data available, push it to the audioChunks array
  rec.ondataavailable = e => {
    let audioChunks = [];
    audioChunks.push(e.data);
    // If the MediaRecorder is no longer recording, process the audio and send it to the server
    if (rec.state == "inactive") {
      // Create a Blob object from the audio chunks
      let blob = new Blob(audioChunks, { type: 'audio/mpeg-3' });
      // Set the source of the audio element to the Blob object
      recordedAudio.src = URL.createObjectURL(blob);
      // Set the audio element to display controls and autoplay
      recordedAudio.controls = true;
      recordedAudio.autoplay = true;
      // Send the audio data to the server for transcription
      sendData(blob)
    }
  }
}

// Define the sendData function to send the audio data to the server
function sendData(blob){
  // Use the fetch API to send a POST request to the server with the audio data in the request body
  fetch('/speech_to_text', {
      method: 'POST',
      body: blob
    })
    // If the request is successful, get the transcription from the server response and display it
    .then(response => response.text())
    .then(transcription => {
      //Display the transcribed text
      document.querySelector("#transcription").textContent = transcription;
      // call the store_voice_transcript function to store the transcription in the database

    })
    // If there is an error, log the error message and display an alert to the user
    .catch(error => {
      console.error(error);
      alert("Error occurred during transcription. Please try again.");
    });
  }







// Add a click event listener to the record button
record.onclick = e => {
  console.log('I was clicked')
  // Disable the record button to prevent multiple recordings
  record.disabled = true;
  // Change the background color of the record button to indicate recording
  record.style.backgroundColor = "#ffcc00"
  // Enable the stop button
  stopRecord.disabled = false;
  // Clear the audioChunks array
  audioChunks = [];
  // Start recording with the MediaRecorder object
  rec.start();
}

// Add a click event listener to the stop button
stopRecord.onclick = e => {
  console.log("I was clicked")
  // Enable the record button
  record.disabled = false;
  // Disable the stop button to prevent multiple stops
  stop.disabled = true;
  // Change the background color of the record button to indicate not recording
  record.style.backgroundColor = "#002f62"
  // Stop recording with the MediaRecorder object
  rec.stop();
}
