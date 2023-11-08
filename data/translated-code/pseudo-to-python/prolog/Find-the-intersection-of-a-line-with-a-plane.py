def main():
    # initialization for the main function
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    
    result = intersect_point(vector1, vector2)
    print(result)

def vector_plus(v1, v2):
    # function to add two vectors
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_minus(v1, v2):
    # function to subtract two vectors
    return [v1[i] - v2[i] for i in range(len(v1))]

def vector_times(v, s):
    # function to multiply a vector by a scalar
    return [v[i] * s for i in range(len(v))]

def vector_dot(v1, v2):
    # function to calculate the dot product of two vectors
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def intersect_point(ray, plane):
    # function to find the intersection point of a ray and a plane
    # implementation goes here

main()