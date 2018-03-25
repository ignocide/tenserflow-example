import inputs
import kmeans

vectors_set = inputs.generate()

[vectors_set,assignment_values] = kmeans.proc(vectors_set)

kmeans.draw(vectors_set, assignment_values)
