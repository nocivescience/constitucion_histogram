from manim import *
class ContScene(Scene):
    CONFIG={
        
    }
    def construct(self):
        rectangulo=Rectangle(height=2,width=1,color=BLUE)
        self.add(rectangulo)
        for i in range(3,10):
            self.play(ApplyMethod(rectangulo.stretch_to_fit_height,i))
        self.wait()