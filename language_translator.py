
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import messagebox
import pyperclip as pc
from gtts import gTTS
import os
import speech_recognition as spr
import pyttsx3
import enchant
import pytesseract
import cv2
from hyperframe import frame
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf


root = tk.Tk()
root.title('Langauge Translator')
root.geometry('1060x660')
root.maxsize(1060, 660)
root.minsize(1060, 660)
title_bar_icon = PhotoImage(file="resources/icons/newlogo.png")
root.iconphoto(False,title_bar_icon)
cl =''
output=''



def cnn_model(h, w):
  inputs = keras.Input(shape=(h, w, 3))
  x = layers.Conv2D(32, (3, 3), activation="relu")(inputs)
  x = layers.MaxPooling2D(pool_size=(2, 2))(x)
  # Add more convolutional and pooling layers as needed
  return keras.Model(inputs=inputs, outputs=x)

# Define the RNN sequence prediction model
def rnn_model(features):
  x = layers.LSTM(64, return_sequences=True)(features)  # You can use LSTM or GRU
  x = layers.LSTM(32)(x)
  outputs = layers.Dense(8, activation="sigmoid")(x)  # 8 for (x1, y1, x2, y2, conf) of 4 corners and confidence score
  return keras.Model(inputs=features, outputs=outputs)

# Combine CNN and RNN models
def create_text_detection_model(h, w):
  cnn_model = cnn_model(h, w)
  features = cnn_model.output
  predictions = rnn_model(features)
  model = keras.Model(inputs=cnn_model.input, outputs=predictions)
  # Define loss function and optimizer (replace with IoU loss for text detection)
  model.compile(loss="mse", optimizer="adam")
  return model

# Preprocess the image
def preprocess_image(image, target_size=(224, 224)):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for model compatibility
  image = cv2.resize(image, target_size)
  image = image.astype("float32") / 255.0
  return np.expand_dims(image, axis=0)

# Process predictions to get bounding boxes (replace with your implementation)
def process_predictions(predictions):
  # Implement logic to convert model output (predictions) into bounding boxes
  # This might involve techniques like Non-Maximum Suppression (NMS)
  # ... (your bounding box processing code)
  # For example, assuming predictions contain coordinates and confidence scores:
  bounding_boxes = []
  for i in range(0, len(predictions), 8):  # Assuming 8 values per box
    x1, y1, x2, y2, conf = predictions[i:i+5]
    if conf > 0.5:  # Set a threshold for confidence score
      bounding_boxes.append((int(x1), int(y1), int(x2), int(y2)))
  return bounding_boxes

# Function to detect text in an image
def detect_text(image, model):
  preprocessed_image = preprocess_image(image)
  predictions = model.predict(preprocessed_image)
  bounding_boxes = process_predictions(predictions)
  return bounding_boxes





def translate():
    language_1 = t1.get("1.0", "end-1c")
    global cl
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
    else:

         t2.delete(1.0, 'end')
         translator = Translator()
         global output
         output = translator.translate(language_1, dest=cl)
         output = output.text
         t2.insert('end', output)




def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')





def camera():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Set up the camera
    cap = cv2.VideoCapture(0)

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale for better OCR results
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform OCR on the grayscale image
        text = pytesseract.image_to_string(gray)

        # If text is detected, print it out
        if text:
            print("Detected text: ", text)
            t1.insert('end', text)

        # Display the captured frame
        cv2.imshow('frame', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()



def texttospeech():
 global cl
 cl = choose_langauge.get()
 if os.path.exists(""):
     # os.remove("text_to_speech.mp3")
     mytext = t1.get("1.0", "end-1c")
     global output;
     engine = pyttsx3.init()
     engine.say(output)
     engine.runAndWait()
 language: str='en'
 if cl == 'English':
     language = 'en'
 elif cl == 'Afrikaans':
     language = 'af'
 elif cl == 'Albanian':
     language = 'sq'
 elif cl == 'Arabic':
     language = 'ar'
 elif cl == 'Armenian':
     language = 'hy'
 elif cl == 'Azerbaijani':
     language = 'az'
 elif cl == 'Basque':
     language = 'eu'
 elif cl == 'Belarusian':
     language = 'be'
 elif cl == 'Bengali':
     language = 'bn'
 elif cl == 'Bosnian':
     language = 'bs'
 elif cl == 'Bulgarian':
     language = 'bg'
 elif cl == 'Catalan':
     language = 'ca'
 elif cl == 'Cebuano':
     language = 'ceb'
 elif cl == 'Chinese':
     language = 'zh'
 elif cl == 'Corsican':
     language = 'co'
 elif cl == 'Croatian':
     language = 'hr'
 elif cl == 'Czech':
     language = 'cs'
 elif cl == 'Danish':
     language = 'da'
 elif cl == 'Dutch':
     language = 'nl'
 elif cl == 'English':
     language = 'en'
 elif cl == 'Esperanto':
     language = 'eo'
 elif cl == 'Estonian':
     language = 'et'
 elif cl == 'Finnish':
     language = 'fi'
 elif cl == 'French':
     language = 'fr'
 elif cl == 'Frisian':
     language = 'fy'
 elif cl == 'Galician':
     language = 'gl'
 elif cl == 'Georgian':
     language = 'ka'
 elif cl == 'German':
     language = 'de'
 elif cl == 'Greek':
     language = 'el'
 elif cl == 'Gujarati':
     language = 'gu'
 elif cl == 'Haitian Creole':
     language = 'ht'
 elif cl == 'Hausa':
     language = 'ha'
 elif cl == 'Hawaiian':
     language = 'haw'
 elif cl == 'Hebrew':
     language = 'he'
 elif cl == 'Hindi':
     language = 'hi'
 elif cl == 'Hmong':
     language = 'hmn'
 elif cl == 'Hungarian':
     language = 'hu'
 elif cl == 'Icelandic':
     language = 'is'
 elif cl == 'Igbo':
     language = 'ig'
 elif cl == 'Indonesian':
     language = 'id'
 elif cl == 'Irish':
     language = 'ga'
 elif cl == 'Italian':
     language = 'it'
 elif cl == 'Japanese':
     language = 'ja'
 elif cl == 'Javanese':
     language = 'jv'
 elif cl == 'Kannada':
     language = 'kn'
 elif cl == 'Kazakh':
     language = 'kk'
 elif cl == 'Khmer':
     language = 'km'
 elif cl == 'Kinyarwanda':
     language = 'rw'
 elif cl == 'Korean':
     language = 'ko'
 elif cl == 'Kurdish':
     language = 'ku'
 elif cl == 'Kyrgyz':
     language = 'ky'
 elif cl == 'Lao':
     language = 'lo'
 elif cl == 'Latin':
     language = 'la'
 elif cl == 'Latvian':
     language = 'lv'
 elif cl == 'Lithuanian':
     language = 'lt'
 elif cl == 'Luxembourgish':
     language = 'lb'
 elif cl == 'Macedonian':
     language = 'mk'
 elif cl == 'Malagasy':
     language = 'mg'
 elif cl == 'Malay':
     language = 'ms'
 elif cl == 'Malayalam':
     language = 'ml'
 elif cl == 'Maltese':
     language = 'mt'
 elif cl == 'Maori':
     language = 'mi'
 elif cl == 'Marathi':
     language = 'mr'
 elif cl == 'Mongolian':
     language = 'mn'
 elif cl == 'Myanmar':
     language = 'my'
 elif cl == 'Nepali':
     language = 'ne'
 elif cl == 'Norwegian':
     language = 'no'
 elif cl == 'Odia':
     language = 'or'
 elif cl == 'Pashto':
     language = 'ps'
 elif cl == 'Persian':
     language = 'fa'
 elif cl == 'Polish':
     language = 'pl'
 elif cl == 'Portuguese':
     language = 'pt'
 elif cl == 'Punjabi':
     language = 'pa'
 elif cl == 'Romanian':
     language = 'ro'
 elif cl == 'Russian':
     language = 'ru'
 elif cl == 'Samoan':
     language = 'sm'
 elif cl == 'Scots Gaelic':
     language = 'gd'
 elif cl == 'Serbian':
     language = 'sr'
 elif cl == 'Sesotho':
     language = 'st'
 elif cl == 'Shona':
     language = 'sn'
 elif cl == 'Sindhi':
     language = 'sd'
 elif cl == 'Sinhala':
     language = 'si'
 elif cl == 'Slovak':
     language = 'sk'
 elif cl == 'Slovenian':
     language = 'sl'
 elif cl == 'Somali':
     language = 'so'
 elif cl == 'Spanish':
     language = 'es'
 elif cl == 'Sundanese':
     language = 'su'
 elif cl == 'Swahili':
     language = 'sw'
 elif cl == 'Swedish':
     language = 'sv'
 elif cl == 'Tajik':
     language = 'tg'
 elif cl == 'Tamil':
     language = 'ta'
 elif cl == 'Tatar':
     language = 'tt'
 elif cl == 'Telugu':
     language = 'te'
 elif cl == 'Thai':
     language = 'th'
 elif cl == 'Turkish':
     language = 'tr'
 elif cl == 'Turkmen':
     language = 'tk'
 elif cl == 'Ukrainian':
     language = 'uk'
 elif cl == 'Urdu':
     language = 'ur'
 elif cl == 'Uyghur':
     language = 'ug'
 elif cl == 'Uzbek':
     language = 'uz'
 elif cl == 'Vietnamese':
     language = 'vi'
 elif cl == 'Welsh':
     language = 'cy'
 elif cl == 'Xhosa':
     language = 'xh'
 elif cl == 'Yiddish':
     language = 'yi'
 elif cl == 'Yoruba':
     language = 'yo'
 elif cl == 'Zulu':
     language = 'zu'
 else:
     language == 'en'
 try:
     myobj = gTTS(text=mytext, lang=language, slow=False)
     myobj.save("text_to_speech.mp3")
     os.system("text_to_speech.mp3")

 except ValueError as e:
     messagebox.showerror('Language Translator', cl+' is currently not supported for Read Aloud (Text to Speech)')
     print(f"An error occurred: {e}")
     # Handle the error or perform any necessary cleanup actions
 except AssertionError as e:
     # Handle the "No text to speak" error
     messagebox.showerror('Language Translator','Please enter the data to be translated before using Read Aloud')
     print("Error:", e)


def speechtotext():
   cl = choose_langauge.get()
   language = 'en'

   if cl == 'English':
       language = 'en'
   elif cl == 'Afrikaans':
       language = 'af'
   elif cl == 'Albanian':
       language = 'sq'
   elif cl == 'Arabic':
       language = 'ar'
   elif cl == 'Armenian':
       language = 'hy'
   elif cl == 'Azerbaijani':
       language = 'az'
   elif cl == 'Basque':
       language = 'eu'
   elif cl == 'Belarusian':
       language = 'be'
   elif cl == 'Bengali':
       language = 'bn'
   elif cl == 'Bosnian':
       language = 'bs'
   elif cl == 'Bulgarian':
       language = 'bg'
   elif cl == 'Catalan':
       language = 'ca'
   elif cl == 'Cebuano':
       language = 'ceb'
   elif cl == 'Chinese':
       language = 'zh'
   elif cl == 'Corsican':
       language = 'co'
   elif cl == 'Croatian':
       language = 'hr'
   elif cl == 'Czech':
       language = 'cs'
   elif cl == 'Danish':
       language = 'da'
   elif cl == 'Dutch':
       language = 'nl'
   elif cl == 'English':
       language = 'en'
   elif cl == 'Esperanto':
       language = 'eo'
   elif cl == 'Estonian':
       language = 'et'
   elif cl == 'Finnish':
       language = 'fi'
   elif cl == 'French':
       language = 'fr'
   elif cl == 'Frisian':
       language = 'fy'
   elif cl == 'Galician':
       language = 'gl'
   elif cl == 'Georgian':
       language = 'ka'
   elif cl == 'German':
       language = 'de'
   elif cl == 'Greek':
       language = 'el'
   elif cl == 'Gujarati':
       language = 'gu'
   elif cl == 'Haitian Creole':
       language = 'ht'
   elif cl == 'Hausa':
       language = 'ha'
   elif cl == 'Hawaiian':
       language = 'haw'
   elif cl == 'Hebrew':
       language = 'he'
   elif cl == 'Hindi':
       language = 'hi'
   elif cl == 'Hmong':
       language = 'hmn'
   elif cl == 'Hungarian':
       language = 'hu'
   elif cl == 'Icelandic':
       language = 'is'
   elif cl == 'Igbo':
       language = 'ig'
   elif cl == 'Indonesian':
       language = 'id'
   elif cl == 'Irish':
       language = 'ga'
   elif cl == 'Italian':
       language = 'it'
   elif cl == 'Japanese':
       language = 'ja'
   elif cl == 'Javanese':
       language = 'jv'
   elif cl == 'Kannada':
       language = 'kn'
   elif cl == 'Kazakh':
       language = 'kk'
   elif cl == 'Khmer':
       language = 'km'
   elif cl == 'Kinyarwanda':
       language = 'rw'
   elif cl == 'Korean':
       language = 'ko'
   elif cl == 'Kurdish':
       language = 'ku'
   elif cl == 'Kyrgyz':
       language = 'ky'
   elif cl == 'Lao':
       language = 'lo'
   elif cl == 'Latin':
       language = 'la'
   elif cl == 'Latvian':
       language = 'lv'
   elif cl == 'Lithuanian':
       language = 'lt'
   elif cl == 'Luxembourgish':
       language = 'lb'
   elif cl == 'Macedonian':
       language = 'mk'
   elif cl == 'Malagasy':
       language = 'mg'
   elif cl == 'Malay':
       language = 'ms'
   elif cl == 'Malayalam':
       language = 'ml'
   elif cl == 'Maltese':
       language = 'mt'
   elif cl == 'Maori':
       language = 'mi'
   elif cl == 'Marathi':
       language = 'mr'
   elif cl == 'Mongolian':
       language = 'mn'
   elif cl == 'Myanmar':
       language = 'my'
   elif cl == 'Nepali':
       language = 'ne'
   elif cl == 'Norwegian':
       language = 'no'
   elif cl == 'Odia':
       language = 'or'
   elif cl == 'Pashto':
       language = 'ps'
   elif cl == 'Persian':
       language = 'fa'
   elif cl == 'Polish':
       language = 'pl'
   elif cl == 'Portuguese':
       language = 'pt'
   elif cl == 'Punjabi':
       language = 'pa'
   elif cl == 'Romanian':
       language = 'ro'
   elif cl == 'Russian':
       language = 'ru'
   elif cl == 'Samoan':
       language = 'sm'
   elif cl == 'Scots Gaelic':
       language = 'gd'
   elif cl == 'Serbian':
       language = 'sr'
   elif cl == 'Sesotho':
       language = 'st'
   elif cl == 'Shona':
       language = 'sn'
   elif cl == 'Sindhi':
       language = 'sd'
   elif cl == 'Sinhala':
       language = 'si'
   elif cl == 'Slovak':
       language = 'sk'
   elif cl == 'Slovenian':
       language = 'sl'
   elif cl == 'Somali':
       language = 'so'
   elif cl == 'Spanish':
       language = 'es'
   elif cl == 'Sundanese':
       language = 'su'
   elif cl == 'Swahili':
       language = 'sw'
   elif cl == 'Swedish':
       language = 'sv'
   elif cl == 'Tajik':
       language = 'tg'
   elif cl == 'Tamil':
       language = 'ta'
   elif cl == 'Tatar':
       language = 'tt'
   elif cl == 'Telugu':
       language = 'te'
   elif cl == 'Thai':
       language = 'th'
   elif cl == 'Turkish':
       language = 'tr'
   elif cl == 'Turkmen':
       language = 'tk'
   elif cl == 'Ukrainian':
       language = 'uk'
   elif cl == 'Urdu':
       language = 'ur'
   elif cl == 'Uyghur':
       language = 'ug'
   elif cl == 'Uzbek':
       language = 'uz'
   elif cl == 'Vietnamese':
       language = 'vi'
   elif cl == 'Welsh':
       language = 'cy'
   elif cl == 'Xhosa':
       language = 'xh'
   elif cl == 'Yiddish':
       language = 'yi'
   elif cl == 'Yoruba':
       language = 'yo'
   elif cl == 'Zulu':
       language = 'zu'
   else:
       language == 'en'

   from_lang = "en"
   to_lang = language

   recog1 = spr.Recognizer()
   mc = spr.Microphone()

   with mc as source:

       recog1.adjust_for_ambient_noise(source, duration=0.9)
       audio = recog1.listen(source)
       get_sentence = recog1.recognize_google(audio)

   try:
       t1.insert("end",get_sentence + "\n")
       translator = Translator()
       text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
       text = text_to_translate.text

       speak = gTTS(text=text, lang=to_lang, slow=False)
       global output
       output = speak.text
       t2.insert("end",output + "\n")
       translate()

   except spr.UnknownValueError:
           t1.insert("Unable to Understand the Input")

   except spr.RequestError as e:
           t1.insert("Unable to provide Required Output".format(e))


# Background Image settings using Tkinter
img = ImageTk.PhotoImage(Image.open('NEWEDITED.png'))
label = Label(image=img)
label.place(x=0, y=0)

a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20,textvariable=a, state='readonly', font=('Corbel', 20, 'bold'), )

auto_detect['values'] = (
    'Auto Detect',
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

auto_detect.place(x=50, y=140)
auto_detect.current(0)
l = tk.StringVar()


choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

choose_langauge.place(x=600, y=140)
choose_langauge.current(0)


translate_text_icon_img = Image.open("resources/icons/documents.png")
resized_translate_text_icon = translate_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
translate_text_icon = ImageTk.PhotoImage(resized_translate_text_icon)

clear_text_icon_img = Image.open("resources/icons/eraser.png")
resized_clear_text_icon = clear_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
clear_text_icon = ImageTk.PhotoImage(resized_clear_text_icon)

camera_text_icon_img = Image.open("resources/icons/copy.png")
resized_copy_text_icon = camera_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
camera_text_icon = ImageTk.PhotoImage(resized_copy_text_icon)

read_aloud_icon_img = Image.open("resources/icons/text_to_speech.png")
resized_read_aloud_icon = read_aloud_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
read_aloud_icon = ImageTk.PhotoImage(resized_read_aloud_icon)

voice_input_icon_img = Image.open("resources/icons/voice_recognition.png")
resized_voice_input_icon = voice_input_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
voice_input_icon = ImageTk.PhotoImage(resized_voice_input_icon)


# Text Widget settings used in Tkinter GUI
t1 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t1.place(x=20, y=200)
t2 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t2.place(x=550, y=200)

# Button settings used in Tkinter GUI
translate_button = Button(root, text=" Translate Text ",image=translate_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=translate,bg="#ffffff")
translate_button.place(x=40, y=565)

clear_button = Button(root, text=" Clear ",image=clear_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
               command=clear,bg="#ffffff")
clear_button.place(x=270, y=565)

# Camera Button settings used in Tkinter GUI
camera_button = Button(root, text=" Camera ",image=camera_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=camera,bg="#ffffff")
camera_button.place(x=485, y=565)

read_aloud = Button(root, text=" Read Aloud ",image=read_aloud_icon, compound="right" ,relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=texttospeech,bg="#ffffff")
read_aloud.place(x=650, y=565)

voice_input = Button(root, text=" Voice Input ", image=voice_input_icon, compound="right", relief=RIDGE, borderwidth=0,
                     font=('Corbel', 20, 'bold'), cursor="hand2", command=speechtotext, bg="#ffffff")
voice_input.place(x=850, y=565)

# Initialize pytesseract


root.mainloop()

