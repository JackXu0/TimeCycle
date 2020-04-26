import os
from shutil import copy

origin_folder = "/Users/zhuocheng/Downloads/DLProject/"

for i in range(0, 133):
    # print(origin_folder + "newdata/scene_"+str(i)+"/")
    # if not os.path.exists(origin_folder + "newdata/scene_"+str(i)+"/"):
    os.makedirs(origin_folder + "/newdata/scene_" + str(i) + "/CAM_FRONT_LEFT/")
    os.makedirs(origin_folder + "/newdata/scene_" + str(i) + "/CAM_FRONT/")
    os.makedirs(origin_folder + "/newdata/scene_" + str(i) + "/CAM_FRONT_RIGHT/")
    os.makedirs(origin_folder + "/newdata/scene_" + str(i) + "/CAM_BACK_LEFT/")
    os.makedirs(origin_folder + "/newdata/scene_" + str(i) + "/CAM_BACK/")
    os.makedirs(origin_folder + "/newdata/scene_" + str(i) + "/CAM_BACK_RIGHT/")
    for j in range(0, 125):
        # print(origin_folder + "/data/scene_"+str(i)+"/sample_"+str(j)+"/CAM_BACK.jpeg")
        # print(origin_folder + "/data/scene_"+str(i)+"/CAM_BACK_"+str(j)+".jpeg")
        copy(origin_folder + "/data/scene_" + str(i) + "/sample_" + str(j) + "/CAM_FRONT_LEFT.jpeg",
                  origin_folder + "/newdata/scene_" + str(i) + "/CAM_FRONT_LEFT/" + str(j) + ".jpeg")
        copy(origin_folder + "/data/scene_" + str(i) + "/sample_" + str(j) + "/CAM_FRONT.jpeg",
                  origin_folder + "/newdata/scene_" + str(i) + "/CAM_FRONT/" + str(j) + ".jpeg")
        copy(origin_folder + "/data/scene_" + str(i) + "/sample_" + str(j) + "/CAM_FRONT_RIGHT.jpeg",
                  origin_folder + "/newdata/scene_" + str(i) + "/CAM_FRONT_RIGHT/" + str(j) + ".jpeg")
        copy(origin_folder + "/data/scene_" + str(i) + "/sample_" + str(j) + "/CAM_BACK_LEFT.jpeg",
                  origin_folder + "/newdata/scene_" + str(i) + "/CAM_BACK_LEFT/" + str(j) + ".jpeg")
        copy(origin_folder + "/data/scene_" + str(i) + "/sample_" + str(j) + "/CAM_BACK.jpeg",
                  origin_folder + "/newdata/scene_" + str(i) + "/CAM_BACK/" + str(j) + ".jpeg")
        copy(origin_folder + "/data/scene_" + str(i) + "/sample_" + str(j) + "/CAM_BACK_RIGHT.jpeg",
                  origin_folder + "/newdata/scene_" + str(i) + "/CAM_BACK_RIGHT/" + str(j) + ".jpeg")
