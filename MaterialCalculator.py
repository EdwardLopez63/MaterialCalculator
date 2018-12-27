# MATERIAL CALCULATOR 
# Calculator that handles calculating material for warehouse
# 
# Written by Edward Lopez 
#
# Allows the user to enter
# ** Type of material
# ** Width 
# ** Pounds Per Foot
# ** Length


def WideFlange(width, poundsPerFoot, length):
    # multiplies POUNDS PER FOOT by LENGTH
    totalWeight = poundsPerFoot * length;
    print ();
    print ("Size: {} {} x {}# x {}'" .format(userProduct, userWidth, userPounds, userLength));
    print ("Weight: {} lbs" .format(totalWeight));


# ex: wf = wide flange
print ('Enter product code: ');
userProduct = input();

# number
print ('Enter width: ');
userWidth = input();
userWidth = int(userWidth);

# number
print ('Enter pounds per foot: ');
userPounds = input();
userPounds = int(userPounds);

# number
print ('Enter length: ');
userLength = input();
userLength = int(userLength);

# calls the function
WideFlange(userWidth,userPounds,userLength);
