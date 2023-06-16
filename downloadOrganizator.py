from PIL import Image
import os

ORIG_FOLDER = 'C:/Users/Facu/Downloads/'
PICTURES_FOLDER = 'C:/Users/Facu/Downloads/Limpieza/Imagenes/'
AUDIO_FOLDER = 'C:/Users/Facu/Downloads/Limpieza/Audio/'
VIDEO_FOLDER = 'C:/Users/Facu/Downloads/Limpieza/Videos/'
DOCUMENTS_FOLDER = 'C:/Users/Facu/Downloads/Limpieza/Documentos/'
RAR_FOLDER = 'C:/Users/Facu/Downloads/Limpieza/Rar/'


if __name__ == "__main__":
    for filename in os.listdir(ORIG_FOLDER):          # hago un bucle for con cada archivo de la carpeta ORIG FOLDER, llamadnolo filename
        name, extension = os.path.splitext(ORIG_FOLDER + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(ORIG_FOLDER + filename)
            picture.save(PICTURES_FOLDER +filename, optimize=True, quality=60)
            os.remove(ORIG_FOLDER + filename) # BORRAMOS EL ARCHIVO DE LA CARPETA ORIGINAL

        
        if extension in [".mp3", ".wav", ".mpeg"]:
      
            os.rename(ORIG_FOLDER + filename, AUDIO_FOLDER + filename)
        
        if extension in [".mp4", ".m4a"]:
            os.rename(ORIG_FOLDER + filename, VIDEO_FOLDER + filename)


        if extension in [".doc", ".pdf", ".exc", ".docx", ".pptx",".osx"]:
            os.rename(ORIG_FOLDER + filename, DOCUMENTS_FOLDER + filename) 

        if extension in [".rar", ".zip"]:
            os.rename(ORIG_FOLDER + filename, RAR_FOLDER + filename)
        
      ##  if extension in [".html", ".htm"]:
        ##    os.remove(ORIG_FOLDER + filename)
        
        else: 
            print("*** NO FILES FOUNDED ***")



