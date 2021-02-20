import numpy as np
import cv2


def pixList_to_graphData(pixList, base, base_pixels):
    # take the list of pixel values and return the value in graph units
    quant_p_pix = base / base_pixels
    return np.array(pixList) * quant_p_pix



def set_graph_coordinates(image_path):
    # image_path = 'xaPre_height_velocity.png'

    global ix, iy
    ix, iy = -1, -1
    IX, IY = [], []

    def update_cursor_pos(event, x, y, flags, param):  # mouse callback function
        global ix, iy
        if event == cv2.EVENT_LBUTTONDOWN:
            # update mouse coordinates
            ix, iy = x, y

    # text settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    textStart = (10, 30)
    fontScale = 0.8
    fontColor = (0, 0, 0)
    lineType = 2

    # text instructions string list
    instructions = [
        'Set vertical axis base start',
        'Set vertical axis base stop',
        'Set vertical axis origin',
        'Set horizontal axis base start',
        'Set horizontal axis base stop',
        'Set horizontal axis origin',
        'Set points. Press Esc when done.']

    # open image
    img = cv2.imread(image_path)  # load image
    imgWidth = img.shape[0]
    cv2.namedWindow('image')  # open window
    cv2.setMouseCallback('image', update_cursor_pos)

    # write first instructions on picture
    counter, Npoints = 0, 0
    cv2.rectangle(img, (textStart[0] - 10, textStart[1] + 10), (imgWidth, 0), (255, 255, 255), -1)
    cv2.putText(img, instructions[counter], textStart, font, fontScale, fontColor, lineType)

    while (1):
        cv2.imshow('image', img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == ord('p'):  # print
            # print(ix,iy, click)
            print(Npoints, IX, IY)

        elif k == ord('s'):  # set
            # add coordinates to lists
            IX.append(ix), IY.append(iy)

            # update instructions
            if counter < 6:
                counter += 1
            else:
                Npoints += 1
            cv2.rectangle(img, (textStart[0] - 10, textStart[1] + 10), (imgWidth, 0), (255, 255, 255), -1)
            cv2.putText(img, instructions[counter], textStart, font, fontScale, fontColor, lineType)

    cv2.destroyAllWindows()

    return np.array(IX), np.array(IY)
