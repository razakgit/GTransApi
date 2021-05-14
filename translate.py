from googletrans import Translator
translator = Translator()

translatedText=translator.translate('ஒரு நல்ல வாய்ப்பு')
print('TranslatedText:'+translatedText.text)
print('Source Language:'+translatedText.src)
print('Dest Language:'+translatedText.dest)
