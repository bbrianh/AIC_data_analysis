import os, cv2, re, random
import numpy as np
from keras.models import load_model
from PIL import Image
import pandas


def predict(image_df, testpath, submitpath):
    # 9 models
    _NUM_OF_MODELS = 9
    model_size = []
    # input your model sizes
    #put the best one in model_size[0] and name it sign0.h5

    # [DO NOT CHANGE] load the CSV file for evaluation
    workpath = submitpath.rsplit('/', 1)[0] + '/'

    # [DO NOT CHANGE] loop all images for evaluation
    final_decision = []
    for index, row in image_df.iterrows():
        # [DO NOT CHANGE] get the image path, imagepath
        imagepath = testpath + 'img/' + row["img"]
        x1 = row["x1"]
        y1 = row["y1"]
        x2 = row["x2"]
        y2 = row["y2"]
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = max(x2, 0)
        y2 = max(y2, 0)

        img = cv2.imread(imagepath, cv2.IMREAD_COLOR)
        img = img[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]

        line = []

        for i in range(_NUM_OF_MODELS):
            model = load_model(workpath + 'sign%d.h5' % i)
            size = model_size[i]

            # [FREE TO UPDATE - begin] The prediction being made by your logic and / or model(s)
            x = cv2.resize(img, (size, size), interpolation=cv2.INTER_CUBIC)
            x = x.astype(np.float32)
            x /= 255
            # x = x.reshape(1, size, size, 3)
            y = model.predict(np.array([x]))
            label = np.argmax(y[0]) + 1
            line.append(label)

            b_count = np.bincount(line)
            mode = np.argmax(b_count)
            count = np.max(b_count)
            if count >= 5:
                ans = mode
            else:
                ans = line[0]

        final_decision.append(ans)

    # [FREE TO UPDATE - end] The prediction being made by your logic and / or model(s)

    # [DO NOT CHANGE] return a list of labels
    print(final_decision)

    return final_decision