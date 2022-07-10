from turtle import right
from manim import *
class ConstScene(Scene):
    CONFIG={
        'axes_config':{
            'x_range':[0,1,1],
            'x_axis_config':{
                'unit_size':1.2,
            },
            'y_range':[0,100,100],
            'y_axis_config':{
                'unit_size':0.065,
                'include_tip':True,
            }
        },
    }
    def construct(self):
        rectangle=Rectangle(height=1,width=1)
        # drawing the axes
        axes_hist=self.get_axes_hist()
        rectangle.move_to(axes_hist.coords_to_point(0,0))
        self.play(FadeIn(axes_hist))
        for i in np.random.random(10):
            self.play(ApplyMethod(rectangle.stretch_to_fit_height,i,about_edge=DOWN))
        self.wait()
    def get_axes_hist(self):
        axes=Axes(**self.CONFIG['axes_config'])
        return axes