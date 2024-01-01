import speech_recognition as sr
import pyttsx3 
import openai

r = sr.Recognizer() 
filename = 'Recording.wav'
openai.api_key = "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"
text = ""

def SpeakText(command):
     
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
     

while(1):    
         
    input = None
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
            
        # get user speach
        audio2 = r.listen(source2)
        
        # convert speach to text
        if audio2:
            input = r.recognize_google(audio2)
            input = input.lower()


        # SpeakText(MyText)
        if input is not None:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Dont let the answer be long, make it very consise and short" + input}], )
            finalResponse = response['choices'][0]['message']['content']
        
        if not 'stop' in input:
            SpeakText(finalResponse)
