import lab

# We'll use the same work file here for all three package/module patterns to
# show that this code need not change.

def compute_circle_areas(radiuses):
    radiuses_squared = lab.square_a_list(radiuses)
    areas = lab.multiply_a_list_by(radiuses_squared, lab.PI)
    return areas


def get_areas_string(areas):
    return 'The areas are: ' + ', '.join(str(area) for area in areas)


circle_radiuses = [1, 2, 8, 10]
circle_areas = compute_circle_areas(circle_radiuses)
result_string = get_areas_string(circle_areas)
print(result_string)
print(lab.backwards(result_string))
