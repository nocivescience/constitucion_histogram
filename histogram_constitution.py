from turtle import right
from manim import *
class ConstScene(Scene):
    CONFIG={
        'axis_config':{
            'x_range':[0,3,1],
            'y_range':[0,100,10],
            'x_axis_config':{
                'unit_size':{
                    'unit_size':1.2
                }
            },
            'y_axis_config':{
                'unit_size':{
                    'unit_size':.065
                },    
            },
            'y_length':4,
            'x_length':7,
        },
        'n_scores':10,
    }
    def construct(self):
        rectangle=Rectangle(height=1,width=1)
        # drawing the axes
        axes_hist=self.get_axes_hist()
        n_scores=self.CONFIG['n_scores']
        random_points=self.get_random_scores()
        scores=np.array([
            random_points
            for _ in range(n_scores)
        ])
        index_tracker=ValueTracker(n_scores)
        def get_index():
            value = np.random.random()*axes_hist.y_axis.unit_size
            return value
        bars=self.get_rectangles(axes_hist)
        bars.add_updater(
            lambda b: self.set_histogram_bars(b,scores[:get_index()],axes_hist)
        )
        self.add(bars,axes_hist)
        index_tracker.set_value(1)
        for value in [10,100]:
            anims=[
                ApplyMethod(
                    index_tracker.set_value,value,
                    rate_func=linear,
                    run_time=5,
                )
            ]
            self.play(*anims)
        self.wait()
    def get_axes_hist(self):
        axes=Axes(**self.CONFIG['axis_config'])
        return axes
    def get_rectangles(self,axes):
        rectangles=VGroup()
        for i in [1,2]:
            coord_rect=axes.coords_to_point(i,0)
            rectangle=Rectangle(width=2).move_to(coord_rect,DOWN).set_fill(color=RED,opacity=1)
            rectangle.i=i
            rectangles.add(rectangle)
        return rectangles
    def get_relative_proportion_map(self, all_scores):
        score=set(all_scores)
        n_scores=len(score)
        return dict([
            (s,np.sum(all_scores==s)/n_scores)
            for s in score
        ])
    def set_histogram_bars(self,bars,scores,axes):
        prop_map=self.get_relative_proportion_map(scores)
        epsilon=1e-6
        for bar in bars:
            prop=prop_map.get(bar.i,epsilon)
            bar.stretch_to_fit_height(
                prop*axes.y_axis.unit_size*100,
                about_edge=DOWN,
            )
    def get_random_scores(self):
        score=1
        radius=1
        while True:
            point =np.random.uniform(-1,1,size=2)
            hit_radius=np.linalg.norm(point)
            if hit_radius>radius:
                return score
            else:
                score+=1
                radius=np.sqrt(radius**2-hit_radius**2)