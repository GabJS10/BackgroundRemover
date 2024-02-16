import os
from datetime import datetime
from rembg import remove
import shutil
class BackgroungRemover:
    def __init__(self,input_folder_name,output_folder_name):
        self.input_folder_name = input_folder_name
        self.output_folder_name = output_folder_name


    def procces_image(self):
        today = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        process_path = os.path.join(self.output_folder_name,today)
        os.makedirs(process_path, exist_ok=True)

        for filename in os.listdir(self.input_folder_name):
            if filename.endswith((".jpg",".png",".jpeg")):
                image_path = os.path.join(self.input_folder_name,filename)
                output_path = os.path.join(process_path,filename)
                self._remove_background(image_path,output_path)
                self._move_original(image_path,process_path)

    def _remove_background(self,image_path,output_path):
        with open(image_path,"rb") as img, open(output_path,"wb") as imgout:
            myimage = img.read()
            rem_back_img = remove(myimage)
            imgout.write(rem_back_img)

    def _move_original(self,path_original,process_path):
         orinals_path = os.path.join(process_path,"originals")
         os.makedirs(orinals_path,exist_ok=True)

         out_filename = os.path.basename(path_original)
         file_out_path = os.path.join(orinals_path,out_filename)

         shutil.move(path_original,file_out_path)


if __name__ == "__main__":
    input = "input"
    output = "output"         

    remover = BackgroungRemover(input_folder_name=input,output_folder_name=output)
    remover.procces_image()
