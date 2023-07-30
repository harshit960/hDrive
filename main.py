import videoConversion as vc
import fileConversion as fc
import uploadBot as ub
import os
import vidUpload as vu
#garbar

if __name__ == "__main__":
    os.system("clear")
    while True:
        print("TubeStore - Convert your data to youtube uploadable video format\n\n")
        print("1. Create video from data\n")
        print("2. Retrieve data from video\n")
        print("3. Exit Program\n")
        option = int(input())
        os.system("clear")
        if option == 1:
            url = input("\nEnter url path:")
            name= str(input("\nTitle of the file: "))
            print("\nProcessing . .")
            [path,extension]=fc.fileSave(url,name)
            [difference,ext,exPath] = vc.binaryToVideo(fc.fileToBinary(path),path,extension)
            #vu.VidUpload(exPath)
            ub.uploadBot(exPath)
            os.system("clear")
            print("Data to Video conversion successfull!\n\n")
        elif option==2:
            path = input("\nEnter video path:")
            print("\nProcessing . .")
            fc.binaryToFile(vc.videoToBinary(path))
            os.system("clear")
            print("Video to Data conversion successfull!\n\n")
        elif option==3:
            os.system("clear")
            exit()

        else:
            pass
        