import speech_recognition as sr
import pyaudio

def tur_spe_recog():
    mikrofon = sr.Microphone()
    kayit = sr.Recognizer()
    
    with mikrofon as ses_dosyasi:
        kayit.adjust_for_ambient_noise(ses_dosyasi)
        ses = kayit.listen(ses_dosyasi)
        try:
            return kayit.recognize_google(ses, language='tr-TR')
        except:
            print("Sesiniz Algılanamadı!")