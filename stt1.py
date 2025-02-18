#source : https://github.com/6figuress/speech_to_text_py
# https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
#ref for speech recognition: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Python program to translate
# speech to text
# currently uses the base key, wich may or may not work, see doc for how to deal with keys

import speech_recognition as sr
import pyttsx3
import sounddevice


# Initialize the recognizer 
r = sr.Recognizer() 

# Loop infinitely for user to
# speak

while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            print("getting audio")
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2,language="fr-FR")
            MyText = MyText.lower()
            print(MyText)
            
    #this error can happen if the speech recognition operation failed, if the key isn't valid, or if there is no internet connection     
    except sr.RequestError as e:
        print("Could not request results")
    
    #this error indicate the audio was not understandable, could be mic issue
    except sr.UnknownValueError:
        print("unknown error occurred")
    #except:
    #    print("an error occured")""

#working speech detection from wav file
"""# open the file
with sr.AudioFile("8842-304647-0013.wav") as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)"""