import cv2
import numpy as np
import sys
import os

boundaries = [[ ([58, 57, 101], [76, 95, 162]) ]]
boundaries += [[ ([26, 61, 111], [81, 144, 202]) ]]
boundaries += [[ ([44, 102, 167], [115, 169, 210]) ]]
boundaries += [[ ([0, 20, 40], [50, 70, 150]) ]]

def getPercent(img):
    totalPicels = img.shape[0] * img.shape[1]
    rustPixels = 0
    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            if img[j,i][0] != 0 and img[j,i][1] != 0 and img[j,i][2] != 0:
                rustPixels += 1
    return (rustPixels / totalPicels) * 100

def processImg(img):
    output = []

    for b in boundaries:
        for (l, u) in b:
            l = np.array(l, dtype = "uint8")
            u = np.array(u, dtype = "uint8")
            mask = cv2.inRange(img, l, u)
            output += [cv2.bitwise_and(img, img, mask = mask)]

    final = output[0]
    for o in output:
        final = cv2.bitwise_or(final, o)
    return final

print("\nRUST DETECTOR")
while(True):

    #cv2.destroyAllWindows()
    path = ''
    choice = ''
    while choice != '1' and choice != '2' and choice != '3':
        print("\nSelect an option:")
        print("1 Detect rust on a single image")
        print("2 Detect rust on several images")
        print("3 Quit")
        choice = input("")

    if choice == '1': # Detect rust on a single image
        choice = ''
        while choice != '1' and choice != '2':
            print("Select the folder where the image is:")
            print("1 Corrosion")
            print("2 No_Corrosion")
            choice = input("")
            if choice == '1':
                path += 'Corrosion/'
            elif choice == '2':
                path += 'No_Corrosion/'

        print('List of files:\n'+str(os.listdir(path)))
        path += input("Insert the image's name: ")
        if not os.path.isfile(path):
            print("Error: Image not found")
            sys.exit()

        img = cv2.imread(path, 1)
        final = processImg(img)

        crop = input("Do you want to crop the image ? (y/n)\n")
        if crop == 'y':
            # Select ROI
            r = cv2.selectROI(img)
            # Crop image
            final = final[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        else:
            cv2.imshow("Original", img)

        rustPercent = getPercent(final)
        print("Percentage of rust in the image: %.2f%%"%rustPercent)
        # Display cropped image
        cv2.imshow("Processed_Image", final)
        # cv2.imshow("final", final)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        #input("")

    elif choice == '2': # Detect rust on several images
        folder = input("Select the folder where the image is:\n") + '/'
        if not os.path.isdir(folder):
            print("Error: Directory not found")
            sys.exit()
        files = os.listdir(folder)
        print(files)
        crop = input("Do you want to set a minimum percentage of rust per image ? (y/n)\n")
        minPercent = 0
        if crop == 'y':
            minPercent = int(input("Insert the minimum percentage\n"))

        finalImgsNames = []
        for f in files:
            img = cv2.imread(folder+f, 1)
            final = processImg(img)
            rustPercent = getPercent(final)
            print(f+" - %.2f%%"%rustPercent)
            if rustPercent >= minPercent:
                finalImgsNames += [f]
        
        print("List of images: ")
        print(finalImgsNames)

    elif choice == '3':
        sys.exit()

            