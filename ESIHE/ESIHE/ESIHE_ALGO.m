function [ ESIHEoutput ] = ESIHE_ALGO( img )
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% All rights reserved.
% This work should only be used for nonprofit purposes.
% Please cite the paper when you use this code:
% Kuldeep Singh, Rajiv Kapoor,"Image enhancement using exposure based sub image histogram equalization",
% Pattern Recogn. Lett. 36 (2014) 10–14.
%
% AUTHORS:
%     Kuldeep Singh,Scientist , Central Research Lab, Bharat Electronics Ltd, India,
%     email:kuldeep.er@gmail.com
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Histogram Calculation
L=256;
x=[0:1:L-1];
[w,l]=size(img); 
len=w*l;
y=reshape(img,len,1);   
xpdf=hist(y,[0:L-1]); 

%% Clipping Process
Tc=mean(xpdf);  % mean pixels for gray levels
Tc=round(Tc);
Ihist=zeros(1,256);   % intermediate histogram for clipping
 for i=1:256
     if xpdf(i)>Tc
     Ihist(i)=Tc;
     elseif xpdf(i)==0
          Ihist(i)=xpdf(i);
     else
         Ihist(i)=xpdf(i);
     end     
 end
%% Exposure Threshold
exposure=sum(xpdf.*x)/sum(xpdf)/(L);
aNorm=(1-exposure);
Xm=round(L*aNorm);
%% ESIHE
ESIHEoutput=zeros(size(img));          
C_L=zeros(1,Xm+1);
C_U=zeros(1,(256-(Xm+1)));
n_L=sum(Ihist(1:Xm+1));
n_U=sum(Ihist(Xm+2:256));
P_L=Ihist(1:Xm+1)/n_L;
P_U=Ihist(Xm+2:256)/n_U;
C_L(1)=P_L(1);
for r=2:length(P_L)
    C_L(r)=P_L(r)+C_L(r-1);
end
C_U(1)=P_U(1);
for r=2:(length(P_U))
    C_U(r)=P_U(r)+C_U(r-1);
end
for r=1:w                       
    for s=1:l
        if img(r,s)<(Xm+1)
            f=Xm*C_L(img(r,s)+1);
            ESIHEoutput(r,s)=round(f);
        else
            f=(Xm+1)+(255-Xm)*C_U((img(r,s)-(Xm+1))+1);
            ESIHEoutput(r,s)=round(f);
        end
    end
end
if strcmp(class(img),'uint8')
    ESIHEoutput = uint8(ESIHEoutput);
elseif strcmp(class(img),'uint16')
     ESIHEoutput = uint16(ESIHEoutput);
elseif strcmp(class(img),'int16')
     ESIHEoutput = int16(ESIHEoutput);
elseif strcmp(class(img),'single')
     ESIHEoutput = single(ESIHEoutput);
end

end