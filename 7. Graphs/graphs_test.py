"""
Filename: graphs_test.py
Desription: Tests the Graph code
Author: Priyankar Shivhare
Date: April 17, 2025
"""
from graphs import Graph

def test_all_functions():
    """Test Graphs Functionality"""
    try:
        my_graph = Graph() # Test Construtor
        assert not my_graph.adj_list
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_graph.add_vertex('D') # Test Add Vortex
        my_graph.add_vertex('E')
        assert 'D' in my_graph.adj_list
        assert 'E' in my_graph.adj_list
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')


    try:
        my_graph.add_edge('D','E') # Test Add Edge (Valid)
        assert my_graph.adj_list['D'] == ['E']
        assert my_graph.adj_list['E'] == ['D']
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert my_graph.add_edge('D','F') is False # Test add egde (Invalid)
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert my_graph.remove_edge('D','F') is False # Test remove egde (Invalid)
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert my_graph.remove_edge('D','E') is True # Test remove egde (Valid)
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert my_graph.remove_edge('D','E') is False # Test remove same egde again
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        my_graph = Graph()
        my_graph.add_vertex('A')
        my_graph.add_vertex('B')
        my_graph.add_vertex('C')
        my_graph.add_edge('A','B')
        my_graph.add_edge('B','C')
        my_graph.add_edge('C','A')
        assert my_graph.adj_list == {'A':['B','C'], 'B':['A','C'], 'C':['B','A']}
        assert my_graph.remove_vertex('A') is True # Test Remove Vertex
        assert my_graph.adj_list == {'B':['C'], 'C':['B']}
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert my_graph.remove_edge('B', 'C') is True
        assert my_graph.remove_vertex('B') is True # Test Remove Vertex with no edges
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert my_graph.remove_vertex('D') is False # Remove Invalid Vertex
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')
test_all_functions()
