import cv2
from face_detector import get_face_detector, find_faces
from face_landmarks import get_landmark_model, detect_marks, draw_marks
face_model = get_face_detector()
landmark_model = get_landmark_model()
outer_points = [[49, 59], [50, 58], [51, 57], [52, 56], [53, 55]]
d_outer = [0]*5
inner_points = [[61, 67], [62, 66], [63, 65]]
d_inner = [0]*3
font = cv2.FONT_HERSHEY_SIMPLEX 
cap = cv2.VideoCapture(0)


class VideoCamera (object):
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)
        
    def __del__(self):
        self.video.release()
        cap.video.release()
        cv2.destroyAllWindows()
        
    # def get_frame(self):
    #     ret, frame = self.vedio.read()
        
    #     ret,jpeg = cv2.imencode('.jpg', frame)
        
    #     return jpeg.tobytes()
    def get_frame(self):
        while(True):
            ret, img = cap.read()
            rects = find_faces(img, face_model)
            for rect in rects:
                shape = detect_marks(img, landmark_model, rect)
                draw_marks(img, shape)
                cv2.putText(img, 'Press r to record Mouth distances', (30, 30), font,
                            1, (0, 255, 255), 2)
                # cv2.imshow("Output", img)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                for i in range(100):
                    for i, (p1, p2) in enumerate(outer_points):
                        d_outer[i] += shape[p2][1] - shape[p1][1]
                    for i, (p1, p2) in enumerate(inner_points):
                        d_inner[i] += shape[p2][1] - shape[p1][1]
                break
            ret,jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()
cv2.destroyAllWindows()
        # ret, frame = self.vedio.read()
        
        # ret,jpeg = cv2.imencode('.jpg', frame)
        
        # return jpeg.tobytes()