import cv2
import numpy as np
import glob
import math

def norm(array):
    # Use norm1 to normalize
    return array / np.linalg.norm(array)
img_names=glob.glob("*.png")
img_names.extend(glob.glob("*.jpg"))
img_names.extend(glob.glob("*.jpeg"))
#training
#using haar cascade classifier for face detection
fc = cv2.CascadeClassifier('hc.xml')
img_mat_count=0
crop_img=[]
g=0
class_vise=[]
read_names=[]
curr=0
for imgs in img_names:
    img_mat=cv2.imread(imgs, 0)
    faces = fc.detectMultiScale(img_mat, 1.3, 5)  #detect faces
    if(type(faces)!=tuple):
        read_names.append(imgs)
        if(read_names[-1][6:8]!=curr):
            class_vise.append([])
            curr=read_names[-1][6:8]
        print(read_names[-1])
        cropped=img_mat[faces[0][1]:faces[0][1]+faces[0][3], faces[0][0]:faces[0][0]+faces[0][2]]  #crop faces
        class_vise[-1].append(cv2.resize(cropped,(128,128)))
        crop_img.append(cv2.resize(cropped,(128,128)))    #resizing the croped face
    img_mat_count+=1
    g+=1
#convert image matrices to vector
img_vect=[]
class_vect=[]
y=0
for each in class_vise:
    class_vect.append([])
    for img in each:
        class_vect[-1].append(img.flatten())
        y+=1
        img_vect.append(img.flatten())
img_vect=np.array(img_vect)
#finding mean of all vectors
mean_vect=np.mean(img_vect, axis = 0)
'''
for x in range(len(img_vect)):
        img_vect[x]=np.subtract(img_vect[x],mean_vect)
'''
'''
m=0
for img in img_vect:
    h=np.reshape(img,(128,128))
    cv2.imshow("a"+str(m), h)
    m+=1
'''
#covariance matrix
C=np.cov(img_vect)
#eigen vectors, values
ev,v=np.linalg.eig(C)
sorted_val=np.sort(ev)
sorted_vec=v[:,ev.argsort()]

for x in range(len(sorted_vec)):
    sorted_vec[x]=norm(sorted_vec[x])

eigmat=[]
for al in range(len(sorted_vec)//10):
    eigmat.append(list(np.matmul(np.array(img_vect).transpose(),sorted_vec[al])))
eigmat=np.array(eigmat)
#eigen faces
'''
y=0
for al in eigmat:
    h=np.reshape(al,(128,128))
    cv2.imshow("a"+str(y), h.astype('uint8'))
    y+=1
'''
for x in range(len(eigmat)):
    eigmat[x]=norm(eigmat[x])
#finding weights
tr_weights=[]
class_weights=[]
for cls in class_vect:
    class_weights.append([])
    for img in cls:
        tr_weights.append([])
        class_weights[-1].append([])
        for vect in eigmat:
            tr_weights[-1].append(img.dot(vect))
            class_weights[-1][-1].append(img.dot(vect))
        
#LDA starts  here
mean_weight=np.mean(tr_weights, axis = 0)

for i in range(len(class_weights)):
    if(len(class_weights[i])==1):
        class_weights.pop(i)

phi=[]
for i in range(len(class_weights)):
    phi.append((np.mean(class_weights[i],axis=0))/len(class_weights[i]))
for i in range(len(phi)):
    for j in range(len(class_weights[i])):
        class_weights[i][j]=np.subtract(class_weights[i][j],phi[i])

sw=[]
for cls in class_weights:
    if(len(cls)==1):
        continue
    sw.append(np.cov(np.array(cls).transpose()))
SW=sw[0]
for each in range(len(sw)-1):
    SW+=sw[each+1]
ph=[]
for i in range(len(phi)):
    phi[i]=np.subtract(phi[i],mean_weight)
    #print(np.matrix(phi[i]).T," ",phi[i])
    ph.append(np.matmul(np.matrix(phi[i]).T,np.matrix(phi[i])))
sb=ph[0]
for i in range(len(ph)-1):
    sb+=ph[i+1]
print('sb',sb)
print(5)
vals, vecs = np.linalg.eig(np.matmul((np.linalg.inv(SW)),sb))

fin_weights=[]
for i in range(len(tr_weights)):
    fin_weights.append(np.matmul(np.array(vecs).transpose(),tr_weights[i]))

print(len(fin_weights[0]))


    

#testing

test_img=glob.glob("tes/*.png")
test_img.extend(glob.glob("tes/*.jpg"))
test_img.extend(glob.glob("tes/*.jpeg"))
tst_mat=[]
img_mat_count=0
img_mat=[]
crop_img=[]
t_read_nms=[]
fc = cv2.CascadeClassifier('hc.xml')
for imgs in test_img:
    img_mat.append(cv2.imread(imgs, 0))
    faces = fc.detectMultiScale(img_mat[img_mat_count], 1.3, 5)  #detect faces
    if(type(faces)!=tuple):
        t_read_nms.append(imgs)
        cropped=img_mat[img_mat_count][faces[0][1]:faces[0][1]+faces[0][3], faces[0][0]:faces[0][0]+faces[0][2]]  #crop faces
        crop_img.append(cv2.resize(cropped,(128,128)))    #resizing the croped face
    img_mat_count+=1
    g+=1
    
#convert image matrices to vector
tst_vect=[]
for img in crop_img:
    tst_vect.append(img.flatten())
#mean vector
#for x in range(len(tst_vect)):
#        tst_vect[x]=np.subtract(tst_vect[x],mean_vect)
#finding weights
ts_weights=[]
for img in tst_vect:
    ts_weights.append([])
    for vect in eigmat:
        ts_weights[-1].append(img.dot(vect))

for i in range(len(ts_weights)):
    ts_weights[i]=(np.matmul(np.array(vecs).transpose(),ts_weights[i]))

#finding most similar image
cnt=0
tt=0
for each in range(len(ts_weights)):
    tt+=1
    dist_mat=[]
    min_val=100000000000
    indx=0
    for al in range(len(fin_weights)):
        dist=np.linalg.norm(np.array(ts_weights[each])-np.array(fin_weights[al]))
        dist_mat.append(dist)
        if(dist<min_val):
            min_val=dist
            indx=al
    print(t_read_nms[each])
    print(read_names[indx])        





    

