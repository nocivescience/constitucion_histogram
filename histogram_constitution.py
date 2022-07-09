from manim import *
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
        'n_scores':5,
    }
    def construct(self):
        axes=Axes(**self.CONFIG['axes_config']).to_edge(DOWN,buff=1)
        rectangles=self.get_histogram_bars(axes)[0]
        texto=self.get_histogram_bars(axes)[1]
        self.play(Create(axes),FadeIn(rectangles),Write(texto)) #hay que sacar los text
        
        self.wait()
    def get_histogram_bars(self,axes):
        bars=VGroup()
        n_scores=self.CONFIG['n_scores']
        index_tracker=ValueTracker(n_scores)
        scores=np.array([self.get_random_height() for i in range(self.CONFIG['n_scores'])])
        def get_index():
            value=np.clip(index_tracker.get_value,0,n_scores-1)
            return int(value)
        set_scores=set(scores)
        sort_score= dict([
            (s,np.sum(scores==s)/n_scores)
            for s in set_scores
        ])
        texto=Text('hola')
        for i,color in zip(range(self.CONFIG['axes_config']['x_range'][1]),self.CONFIG['colors']):
            bar=Rectangle(height=scores[i],width=self.CONFIG['axes_config']['x_range'][2]+3,color=BLUE).set_fill(color,1).move_to(axes.c2p(i+1,0),DOWN)
            bars.add(bar)
        return [bars,texto]
    def get_random_height(self):
        score=1
        radius=1
        while True:
            scale=np.random.uniform(-1,1,size=2)
            hit_radius=np.linalg.norm(scale)
            if  hit_radius>radius:
                return score
            else:
                score+=1
                radius=np.sqrt(radius**2-hit_radius**2)