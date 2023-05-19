import sys
sys.path.insert(0, 'src')
import createflow
import test_ML_model

class Test_flowgraph:
    model = test_ML_model.model_load()
    flowgraph = createflow.graph()

    def test_one(self):
        x = [5,5]
        assert self.model.predict([x])[0][0].round(5) == self.flowgraph.propagate([x])[0][0].round(5)

    def test_two(self):
        x = [1,2]
        assert self.model.predict([x])[0][0].round(5) == self.flowgraph.propagate([x])[0][0].round(5)
        
    def test_three(self):
        x = [10,0]
        assert self.model.predict([x])[0][0].round(5) == self.flowgraph.propagate([x])[0][0].round(5)
    
    def test_four(self):
        x = [3,2]
        assert self.model.predict([x])[0][0].round(5) == self.flowgraph.propagate([x])[0][0].round(5)

    def test_five(self):
        x = [8,2]
        assert self.model.predict([x])[0][0].round(5) == self.flowgraph.propagate([x])[0][0].round(5)