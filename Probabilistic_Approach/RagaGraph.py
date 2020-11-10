from .ShortestDistance import shortestDistance


def constructRagaGraph(ragaName):
    if ragaName == 'mohanam':
        RagaGraph = {
            1: [1, 2],
            2: [1, 2, 3],
            3: [2, 3, 4],
            4: [3, 4, 5],
            5: [4, 5, 6],

            6: [5, 6, 7],
            7: [6, 7, 8],
            8: [7, 8, 9],
            9: [8, 9, 10],
            10: [9, 10, 11],

            11: [10, 11, 12],
            12: [11, 12, 13],
            13: [12, 13, 14],
            14: [13, 14, 15],
            15: [14, 15]
        }
        distanceMatrix = [
            [shortestDistance(RagaGraph, i, j) for j in range(1, 16)] for i in range(1, 16)]
    elif ragaName == 'kalyani':
        RagaGraph = {
            1: [1, 2],
            2: [1, 2, 3],
            3: [2, 3, 4],
            4: [3, 4, 5],
            5: [4, 5, 6],
            6: [5, 6, 7],
            7: [6, 7, 8],
            8: [7, 8, 9],
            9: [8, 9, 10],
            10: [9, 10, 11],
            11: [10, 11, 12],
            12: [11, 12, 13],
            13: [12, 13, 14],
            14: [13, 14, 15],
            15: [14, 15, 16],
            16: [15, 16, 17],
            17: [16, 17, 18],
            18: [17, 18, 19],
            19: [18, 19, 20],
            20: [19, 20, 21],
            21: [20, 21]
        }
        distanceMatrix = [
            [shortestDistance(RagaGraph, i, j) for j in range(1, 22)] for i in range(1, 22)]
    elif ragaName == "panthuvarali":
        RagaGraph = {
            1: [1, 2],
            2: [1, 2, 3],
            3: [2, 3, 4],
            4: [3, 4, 5],
            5: [4, 5, 6],
            6: [5, 6, 7],
            7: [6, 7, 8],
            8: [7, 8, 9],
            9: [8, 9, 10],
            10: [9, 10, 11],
            11: [10, 11, 12],
            12: [11, 12, 13],
            13: [12, 13, 14],
            14: [13, 14, 15],
            15: [14, 15, 16],
            16: [15, 16, 17],
            17: [16, 17, 18],
            18: [17, 18, 19],
            19: [18, 19, 20],
            20: [19, 20, 21],
            21: [20, 21]
        }
        distanceMatrix = [
            [shortestDistance(RagaGraph, i, j) for j in range(1, 22)] for i in range(1, 22)]
    elif ragaName == "saveri":
        RagaGraph = {
            1: [1, 2],
            2: [1, 2, 4],
            3: [2, 3],
            4: [3, 4, 5],
            5: [4, 5, 6],
            6: [5, 6, 8],
            7: [6, 7],

            8: [7, 8, 9],
            9: [8, 9, 11],
            10: [9, 10],
            11: [10, 11, 12],
            12: [11, 12, 13],
            13: [12, 13, 15],
            14: [13, 14],

            15: [14, 15, 16],
            16: [15, 16, 18],
            17: [16, 17],
            18: [17, 18, 19],
            19: [18, 19, 20],
            20: [19, 20],
            21: [20, 21]
        }
        distanceMatrix = [
            [shortestDistance(RagaGraph, i, j) for j in range(1, 22)] for i in range(1, 22)]
    elif ragaName == "shankarabharanam":
        RagaGraph = {
            1: [1, 2],
            2: [1, 2, 3],
            3: [2, 3, 4],
            4: [3, 4, 5],
            5: [4, 5, 6],
            6: [5, 6, 7],
            7: [6, 7, 8],
            8: [7, 8, 9],
            9: [8, 9, 10],
            10: [9, 10, 11],
            11: [10, 11, 12],
            12: [11, 12, 13],
            13: [12, 13, 14],
            14: [13, 14, 15],
            15: [14, 15, 16],
            16: [15, 16, 17],
            17: [16, 17, 18],
            18: [17, 18, 19],
            19: [18, 19, 20],
            20: [19, 20, 21],
            21: [20, 21]
        }
        distanceMatrix = [
            [shortestDistance(RagaGraph, i, j) for j in range(1, 22)] for i in range(1, 22)]
    elif ragaName == "thodi":
        RagaGraph = {
            1: [1, 2],
            2: [1, 2, 3],
            3: [2, 3, 4],
            4: [3, 4, 5],
            5: [4, 5, 6],
            6: [5, 6, 7],
            7: [6, 7, 8],
            8: [7, 8, 9],
            9: [8, 9, 10],
            10: [9, 10, 11],
            11: [10, 11, 12],
            12: [11, 12, 13],
            13: [12, 13, 14],
            14: [13, 14, 15],
            15: [14, 15, 16],
            16: [15, 16, 17],
            17: [16, 17, 18],
            18: [17, 18, 19],
            19: [18, 19, 20],
            20: [19, 20, 21],
            21: [20, 21]
        }
        distanceMatrix = [
            [shortestDistance(RagaGraph, i, j) for j in range(1, 22)] for i in range(1, 22)]
    return distanceMatrix
