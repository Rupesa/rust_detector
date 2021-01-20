import cv2
import numpy as np

path = '/Users/ruisantos/Desktop/ano4/cv/rust_detector/'

print("RUST DETECTOR")
print("Select the folder where the image is:")
print("1- Corrosion")
print("2- No_Corrosion")
choice = input("")
if choice == '1':
    path += 'Corrosion/'
elif choice == '2':
    path += 'No_Corrosion/'
path += input("Insert the image's name: ")

img = cv2.imread(path, 1)

#Read the Rust Photograph
#img = cv2.imread('/Users/ruisantos/Desktop/ano4/cv/rust_detector/Corrosion/16.jpg', 1)

#Set different boundaries for different shades of rust
boundaries1 = [ ([58, 57, 101], [76, 95, 162]) ]
boundaries2 = [ ([26, 61, 111], [81, 144, 202]) ]
boundaries3 = [ ([44, 102, 167], [115, 169, 210]) ]
boundaries4 = [ ([0, 20, 40], [50, 70, 150]) ]
#boundaries4 = [ ([0, 0, 0], [255, 255, 255]) ]

#Highlight out the shades of rust
for (lower1, upper1) in boundaries1:
    lower1 = np.array(lower1, dtype = "uint8")
    upper1 = np.array(upper1, dtype = "uint8")
    mask = cv2.inRange(img, lower1, upper1)
    output1 = cv2.bitwise_and(img, img, mask = mask)

#cv2.imshow("Output 1:", output1)

for (lower2, upper2) in boundaries2:
    lower2 = np.array(lower2, dtype = "uint8")
    upper2 = np.array(upper2, dtype = "uint8")
    mask = cv2.inRange(img, lower2, upper2)
    output2 = cv2.bitwise_and(img, img, mask = mask)

#cv2.imshow("Output 2:", output2)

for (lower3, upper3) in boundaries3:
    lower3 = np.array(lower3, dtype = "uint8")
    upper3 = np.array(upper3, dtype = "uint8")
    mask = cv2.inRange(img, lower3, upper3)
    output3 = cv2.bitwise_and(img, img, mask = mask)

#cv2.imshow("Output 3:", output3)

for (lower4, upper4) in boundaries4:
    lower4 = np.array(lower4, dtype = "uint8")
    upper4 = np.array(upper4, dtype = "uint8")
    mask = cv2.inRange(img, lower4, upper4)
    output4 = cv2.bitwise_and(img, img, mask = mask)

#cv2.imshow("Output 4:", output4)

new = []
#print(img[50,50])
# for j in range(img.shape[0]):
#     for i in range(img.shape[1]):
#         #print(img[j,i][0])
#         #if img[j,i][0] in range([40, 20, 0], [190, 169, 97]):
#         if img[j,i][0] in range(40, 129):
#             new = []
#         else:
#             img[j,i] = [0,0,0]

# cv2.imshow("img", img)

# for l in img:
#     for c in l:
#         new[]


#Combine the 3 different masks with the different shades into 1 image file
final = cv2.bitwise_or(output1, output2, output3)
final = cv2.bitwise_or(final, output4)

cv2.imshow("original", img)
cv2.imshow("final", final)
cv2.waitKey(0)