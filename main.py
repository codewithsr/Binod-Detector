import os

def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():
        return True

    else:
        return False

if __name__ == "__main__":
    #Listing the contents of this folder
    dir_contents = os.listdir()

    nBinod = 0
#For each text file, run isBinod for them
    for items in dir_contents:
        if items.endswith('txt'):
            print(f"**********Detecting Binod in {items}!!!!!!!")
            flag = isBinod(items)
            if(flag):
                print(f"Binod found in {items}")
                nBinod += 1
            else:
                print(f"Binod not found in {items}")

    print("******Binod Detector Summary******")
    print(f"{nBinod} files found with Binod hidden into them")