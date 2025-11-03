print('\n') 

from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('James', 'Jannet')
    assert formatted_name == 'James Jannet'

