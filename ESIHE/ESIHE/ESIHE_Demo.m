img=imread('fish2.jpg');
 if(size(img,3)~=1)
    img = rgb2gray(img);
    img=uint8(img);
 end
imshow(img,[]);xlabel('Original')
ESIHEoutput=ESIHE_ALGO(img);
figure
imshow(ESIHEoutput,[]);xlabel('ESIHE')
