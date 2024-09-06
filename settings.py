# -*- coding: utf-8 -*-

DETECTION_BLUR_KERNEL_SIZE_FOR_EQUATORIAL_MOUNTED_IMAGES = 3
DETECTION_BLUR_KERNEL_SIZE_FOR_FIXED_TRIPOD_IMAGES = 5
# DETECTION_BLUR_KERNEL_SIZE_FOR_DIRECT_METHOD = 11
DETECTION_CANNY_LOW_THRESHOLD = 50
DETECTION_CANNY_RATIO = 3
DETECTION_CANNY_KERNEL_SIZE = 3
DETECTION_LINE_THRESHOLD = 20
DETECTION_LINE_MIN_LINE_LENGTH = 30
DETECTION_LINE_MAX_LINE_GAP = 7

# DETECTION_CROP_IMAGE_BOX_SIZE = 640
DETECTION_CROP_IMAGE_BOX_SIZE = 256

# If cropped image size > DETECTION_CROP_IMAGE_BOX_SIZE * ratio
# will be divided to mosaic images, so as to improve the resolution
RATIO_FOR_MOSAIC = 1.5

# When dividing a big image to mosaic, each image would need
# to have some overlap.
# This ratio is about how much (of the width or height) of
# two images to be overlapped
# Value from 0 to 1
# MOSAIC_OVERLAP_RATIO = 0.5
MOSAIC_OVERLAP_RATIO = 0.25

# To ensure the detected object is within the cropped image, would
# need to enlarge the detection box
# DETECTION_CROP_IMAGE_BOX_FACTOR = 1.5
DETECTION_CROP_IMAGE_BOX_FACTOR = 3.0

# When merging two detection box, need to have some level of overlap
# This threshold means the centers in both dimension need to be less
# than (box1_width + box2_width) * threshold
# BOX_OVERLAP_THRESHOLD = 0.5
BOX_OVERLAP_THRESHOLD = 0.2

# =============================================================================
# For checking false detection
#
# If the detected lines are very closed, and be parallel
# with the border, ignore them
# Value is # of pixels
DETECTION_IMAGE_BORDER_THRESHOLD = 4
LINE_X_OR_Y_DELTA_THRESHOLD = 3

# Get some points around the center of the detected line
# Get those points' color, to check if RGB(0,0,0) which
# means it is on the edge
# Value is # of pixels
LINE_CENTER_RADIUS_CHECKING = 6

# If the pixel color is less than this value, consider it is from the border
DETECTION_BORDER_COLOR_THRESHOLD = 9

# =============================================================================
# For merging two short lines which should belong to the same one
#
# 1 )Acceptable angle delta (in rad, 0.01 rad is around 0.6 degree)
#    Value is angel in rad
#    ~ 23 deg
LINE_ANGEL_DELTA_THRESHOLD = 0.4

# 2) If the two lines are closed enough
# Value is # of pixels
# Would need to consider changing this to ration(% of img size)
LINE_VERTICAL_DISTANCE_FOR_MERGE_THRESHOLD = 8
LINE_VERTICAL_DISTANCE_FOR_MERGE_W_OVERLAP_THRESHOLD = 3
# ~0.06 of the img width
LINE_DISTANCE_FOR_MERGE_THRESHOLD = 300

# May not use this one
LINE_JOINT_ANGEL_DELTA_THRESHOLD = 0.4

# =============================================================================
# For satellite checking
#
# If two lines (have similar angel) are closed enough
# to be considered as satellite
# Value is # of pixels
# Would need to consider changing this to ration(% of img size)
# And would need to be calculated from
#   1) Lens' focal length (different angle width)
#   2) Image interval (# of sec)
LINE_VERTICAL_DISTANCE_FOR_SATELLITE_THRESHOLD = 12
LINE_DISTANCE_FOR_SATELLITE_THRESHOLD = 300

# =============================================================================
# For meteor object extraction
#
# To avoid the dark boundary of the extracted meteor object is too thick.
# If the specific pixel has RGB value lower than this threshold, it will
# be replaced with transparent background.
#
# This value would need to be adjusted according to the brightness of the
# background image
#
# - If the extracted meteor object got cut in the head/tail too much, try to
#   lower this value (as long as the mask file covers the meteor body).
# - If the extracted meteor object has the edge too thick/too dark compare
#   to the star background image, try to increase this value (better to be
#   within 80).
EXTRACT_RGB_VALUE_THRESHOLD = 48

# =============================================================================
# For multi-thread processing
# To avoid memory exhaustion sometimes we need to control the maximum core #
#
# 2021-8-18: It seems the exe will run fail if we needs over 12 threads.
#            Don't know why but just limit the CPU # to 8 at present.
#            But running in IDE environment is no problem.
MAX_CPU_FOR_DETECTION = 12
MAX_CPU_FOR_MASK_EXTRACTION = 12

# =============================================================================
# The Neural Network
CNN_IMAGE_SIZE = 256

# 2020-10-25: This model weight seems to have the best performance on one test set
CNN_SAVED_MODEL = "./saved_model/cnn_star_256_20201025_1_cnn11_lre-4_.731-0.00002.hdf5"

UNET_IMAGE_SIZE = 256

# 2021-03-15: Newer trained model for UNET++. Test result is quite good
UNET_SAVED_MODEL = (
    "./saved_model/unet++_meteor_gray256_20210314-3_wo_val.297-0.201.hdf5"
)
