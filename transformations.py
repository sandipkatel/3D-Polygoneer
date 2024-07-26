from main import SendUI


class Transformation:
    translationValue = 5
    scaleLessValue = 0.9
    scaleMoreValue = 1.111111
    rotationValue = 5

    def move_x_left(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.moveObject(-self.translationValue, 0, 0)
            SendUI(drawing.GetAttributes())

    def move_x_right(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.moveObject(self.translationValue, 0, 0)
            SendUI(drawing.GetAttributes())

    def move_z_front(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.moveObject(0, 0, self.translationValue)
            SendUI(drawing.GetAttributes())

    def move_z_back(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.moveObject(0, 0, -self.translationValue)
            SendUI(drawing.GetAttributes())

    def move_y_up(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.moveObject(0, self.translationValue, 0)
            SendUI(drawing.GetAttributes())

    def move_y_down(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.moveObject(0, -self.translationValue, 0)
            SendUI(drawing.GetAttributes())

    def scale_x_less(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.scaleObject(self.scaleLessValue, 1, 1)
            SendUI(drawing.GetAttributes())

    def scale_x_more(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.scaleObject(self.scaleMoreValue, 1, 1)
            SendUI(drawing.GetAttributes())

    def scale_z_less(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.scaleObject(1, 1, self.scaleLessValue)
            SendUI(drawing.GetAttributes())

    def scale_z_more(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.scaleObject(1, 1, self.scaleMoreValue)
            SendUI(drawing.GetAttributes())

    def scale_y_less(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.scaleObject(1, self.scaleLessValue, 1)
            SendUI(drawing.GetAttributes())

    def scale_y_more(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.scaleObject(1, self.scaleMoreValue, 1)
            SendUI(drawing.GetAttributes())

    def rot_x_left(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.rotObjectX(-self.rotationValue)
            SendUI(drawing.GetAttributes())

    def rot_x_right(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.rotObjectX(self.rotationValue)
            SendUI(drawing.GetAttributes())

    def rot_z_front(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.rotObjectZ(self.rotationValue)
            SendUI(drawing.GetAttributes())

    def rot_z_back(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.rotObjectZ(-self.rotationValue)
            SendUI(drawing.GetAttributes())

    def rot_y_up(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.rotObjectY(self.rotationValue)
            SendUI(drawing.GetAttributes())

    def rot_y_down(self, event, drawing):
        if drawing.objectSelected is not None:
            drawing.rotObjectY(-self.rotationValue)
            SendUI(drawing.GetAttributes())
