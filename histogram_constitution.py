from manim import *
class ShowDistributionOfScores(Scene):
    CONFIG = {
        "axes_config": {
            'x_range':[0,3,1],
            "x_axis_config": {
                "unit_size": 1.2,
            },
            'y_range':[0,100,10],
            "y_axis_config": {
                "unit_size": 0.02,
                "include_tip": False,
            },
        },
        "random_seed": 1,
    }

    def construct(self):
        axes=self.get_hist_axes()
        bars=self.get_histogram(axes)
        bars_random=self.set_update_hist(bars)
        bars_random.add_updater(self.set_update_hist)
        self.add(axes,bars)
        self.wait()
    def get_hist_axes(self):
        axes=Axes(**self.CONFIG['axes_config'])
        axes.set_stroke(width=0.5)
        return axes
    def get_histogram(self,axes):
        bars=VGroup()
        for i in [1,2]:
            bar=Rectangle(width=self.CONFIG['axes_config']['x_axis_config']['unit_size'],height=5,color=BLUE)
            bar.move_to(axes.coords_to_point(i,0),DOWN)
            bars.add(bar)
        return bars
    def set_update_hist(self,bars):
        bar_random=bars.copy().stretch_to_fit_height(np.random.random()*100,about_edge=DOWN)
        bars.become(bar_random)
        return bar_random
            
            