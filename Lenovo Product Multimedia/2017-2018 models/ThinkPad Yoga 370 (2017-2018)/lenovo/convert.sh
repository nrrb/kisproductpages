#!/bin/bash
mkdir -p 750x500
mkdir -p 700x300
# The originals are 1060x596
for i in *.jpg;
do 
    # because we want to match the target aspect ratio of 750x500, we must pad the original
    # on the top and bottom to be (1060*500/750) = 707 pixels tall
    sips --padToHeightWidth 707 1060 --padColor FFFFFF $i --out 750x500/$i; 
    sips -Z 750 750x500/$i --out 750x500/$i;
    sips -g pixelWidth -g pixelHeight 750x500/$i;
##    open 750x500/$i;
    
    # because we want to match the target aspect ratio of 700x300, we must pad the original
    # on the left and right to (596*700/300) = 1391 pixels wide
    sips --padToHeightWidth 596 1391 --padColor FFFFFF $i --out 700x300/$i;
    sips -Z 700 700x300/$i --out 700x300/$i;
    sips -g pixelWidth -g pixelHeight 700x300/$i;
##    open 700x300/$i;
done
