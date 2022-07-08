from cloup import constraint
from manim import *
from matplotlib.pyplot import bar
class HistConstitucionScene(Scene):
    CONFIG={
        'axes_config':{
            'x_range':[0,3,1],
            'x_axis_config':{
                'include_numbers':True,
            },
            'y_axis_config':{
                'include_numbers':True,
            },
            'y_range':[0,100,20],   
            'y_length':5,
        },
        'colors':[BLUE,RED],
    }
    def construct(self):
        axes=Axes(**self.CONFIG['axes_config']).to_edge(DOWN,buff=1)
        rectangles=self.get_histogram_bars(axes)
        self.play(Create(axes),FadeIn(rectangles))
        self.wait()
    def get_histogram_bars(self,axes):
        bars=VGroup()
        random_height=self.get_height()
        for i,color in zip(range(self.CONFIG['axes_config']['x_range'][1]),self.CONFIG['colors']):
            bar=Rectangle(height=random_height[i],width=self.CONFIG['axes_config']['x_range'][2]+3,color=BLUE).set_fill(color,1).move_to(axes.c2p(i+1,0),DOWN)
            bars.add(bar)
        return bars
    def get_height(self):
        number_scores=10000
        