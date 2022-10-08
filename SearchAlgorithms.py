from Space import *
from Constants import *


def is_Exist(arr: list[Node], val: Node):
    for i in range(0, len(arr)):
        if arr[i].value == val.value:
            return True

    return False


def printList(list: list[Node]):
    node = []
    for index in list:
        node.append(index.value)

    print(node)


def distanceNode(node1: Node, node2: Node):
    return sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))


def set_Color_Path(g: Graph, path: [], sc: pygame.surface):

    g.re_draw(g.goal, grey, sc)
    prev = g.goal.value
    while prev != g.start.value:
        pygame.draw.line(sc, green, (g.grid_cells[prev].x, g.grid_cells[prev].y), (
            g.grid_cells[path[prev]].x, g.grid_cells[path[prev]].y), 2)
        pygame.display.flip()
        prev = path[prev]
        g.re_draw(g.grid_cells[prev], grey, sc)
        # path[i].set_color(grey)


""" def findMinCost(g: Graph, l: list[Node]):
    min = 99999
    result: Node = l[0]
    for index in l:
        if min > g.calculatorCost(index):
            min = g.calculatorCost(index)
            result = index

    return result """


def returnMinNodeCostWithHeuristic(g: Graph, open_set: list[Node], cost: []):
    min = 99999
    result = open_set[0]
    for node in open_set:
        if min > cost[node.value] + g.heuristic(node):
            min = cost[node.value] + g.heuristic(node)
            result = node

    return result


def returnNodeMinCost(g: Graph, open_set: list[Node], cost: []):
    min = 99999
    result = open_set[0]
    for node in open_set:
        if min > cost[node.value]:
            min = cost[node.value]
            result = node
    print(min)
    return result


def BFS_algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], father: [], sc: pygame.surface):
    if len(open_set) == 0:
        return

    current_List: list[Node] = []
    current_List = current_List + open_set
    while len(current_List) != 0:
        current_Node: Node = current_List[0]
        if current_Node.value != g.start.value:
            g.re_draw(current_Node, yellow, sc)
        # kiểm tra xem tìm thấy node cần tìm chưa
        # nếu tìm thấy r => bôi màu rgey đường đi
        # nếu chưa thì kiểm thêm node đang xét vào closed, xóa khỏi open
        # thêm vào open các neighbors của node
        if g.is_goal(current_Node):
            set_Color_Path(g, father, sc)
            return

        # thêm vào closed_set
        open_set.remove(current_Node)
        closed_set.append(current_Node)
        current_List.remove(current_Node)
        # current_Node.set_color(blue)
        # thêm vào open_set
        neighbors: list[Node] = g.get_neighbors(current_Node)
        while len(neighbors) != 0:
            if not is_Exist(closed_set, neighbors[0]):
                if not is_Exist(open_set, neighbors[0]):
                    if neighbors[0].value != g.goal.value:
                        g.re_draw(neighbors[0], red, sc)
                    open_set.append(neighbors[0])
                    father[neighbors[0].value] = current_Node.value

            neighbors.remove(neighbors[0])

        if current_Node.value != g.start.value:
            g.re_draw(current_Node, blue, sc)

    BFS_algorithm(g, open_set, closed_set, father, sc)


def DFS_algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], father: [], sc: pygame.surface):
    if len(open_set) == 0:
        return

    # lấy điểm gần nhất được mở tới
    current_Node: Node = open_set[len(open_set) - 1]
    if current_Node.value != g.start.value:
        g.re_draw(current_Node, yellow, sc)

    if (g.is_goal(current_Node)):
        set_Color_Path(g, father, sc)
        return

    # xóa điểm đó khỏi tập mở và thêm vào tập đóng
    open_set.remove(current_Node)
    closed_set.append(current_Node)

    # tạo ra tập chứa các neighbors
    # thêm vào sau open_set khi điểm đó k có trong open_set và closed_set
    neighbors: list[Node] = g.get_neighbors(current_Node)
    while len(neighbors) != 0:
        if not is_Exist(closed_set, neighbors[len(neighbors) - 1]):
            if not is_Exist(open_set, neighbors[len(neighbors) - 1]):
                if neighbors[len(neighbors) - 1].value != g.goal.value:
                    g.re_draw(neighbors[len(neighbors) - 1], red, sc)
                open_set.append(neighbors[len(neighbors) - 1])
                father[neighbors[len(neighbors) -
                                 1].value] = current_Node.value

        neighbors.remove(neighbors[len(neighbors) - 1])

    # tô lại màu
    if current_Node.value != g.start.value:
        g.re_draw(current_Node, blue, sc)

    DFS_algorithm(g, open_set, closed_set, father, sc)


def UCS_algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], cost: [], father: [], sc: pygame.surface):
    if len(open_set) == 0:
        return
    # printList(open_set)
    # xác định điểm xét tới
    current_Node: Node = returnNodeMinCost(g, open_set, cost)
    if current_Node.value != g.start.value:
        g.re_draw(current_Node, yellow, sc)

    # kiểm tra xem điểm đang xét có phải là goal không
    if g.is_goal(current_Node):
        set_Color_Path(g, father, sc)
        return

    # xóa khỏi open_set và thêm vào closed_set
    open_set.remove(current_Node)
    closed_set.append(current_Node)

    # kiểm tra các biên và update cost
    neighbors: list[Node] = g.get_neighbors(current_Node)
    while len(neighbors) != 0:
        if not is_Exist(closed_set, neighbors[0]):
            if not is_Exist(open_set, neighbors[0]):
                if neighbors[0].value != g.goal.value:
                    g.re_draw(neighbors[0], red, sc)
                cost[neighbors[0].value] = cost[current_Node.value] + \
                    distanceNode(current_Node, neighbors[0])
                open_set.append(neighbors[0])
                father[neighbors[0].value] = current_Node.value

        neighbors.remove(neighbors[0])

    if current_Node.value != g.start.value:
        g.re_draw(current_Node, blue, sc)
    UCS_algorithm(g, open_set, closed_set, cost, father, sc)


def AStar_Algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], cost: [], father: [], sc: pygame.surface):
    if len(open_set) == 0:
        return

    # xác định điểm xét tới
    current_Node: Node = returnMinNodeCostWithHeuristic(g, open_set, cost)
    if current_Node.value != g.start.value:
        g.re_draw(current_Node, yellow, sc)

    # kiểm tra xem điểm đang xét có phải là goal không
    if g.is_goal(current_Node):
        set_Color_Path(g, father, sc)
        return

    # xóa khỏi open_set và thêm vào closed_set
    open_set.remove(current_Node)
    closed_set.append(current_Node)

    # kiểm tra các biên và update cost
    neighbors: list[Node] = g.get_neighbors(current_Node)
    while len(neighbors) != 0:
        if not is_Exist(closed_set, neighbors[0]):
            if not is_Exist(open_set, neighbors[0]):
                if neighbors[0].value != g.goal.value:
                    g.re_draw(neighbors[0], red, sc)
                cost[neighbors[0].value] = cost[current_Node.value] + \
                    distanceNode(current_Node, neighbors[0])
                open_set.append(neighbors[0])
                father[neighbors[0].value] = current_Node.value

        neighbors.remove(neighbors[0])

    if current_Node.value != g.start.value:
        g.re_draw(current_Node, blue, sc)
    AStar_Algorithm(g, open_set, closed_set, cost, father, sc)


def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    # nút mở với bắt đầu là điểm bắt đầu
    # tập đóng ???
    # tạo ra 1 array với len = len(g)
    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []
    father: list[Node] = []
    father = [-1]*g.get_len()

    DFS_algorithm(g, open_set, closed_set, father, sc)
    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    """ raise NotImplementedError('Not implemented') """


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    BFS_algorithm(g, open_set, closed_set, father, sc)


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    father = [-1]*g.get_len()
    cost = [0]*g.get_len()
    cost[g.start.value] = 0

    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []

    UCS_algorithm(g, open_set, closed_set, cost, father, sc)
    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    """ raise NotImplementedError('Not implemented') """


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    father = [-1]*g.get_len()
    cost = [0]*g.get_len()
    cost[g.start.value] = 0

    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []

    AStar_Algorithm(g, open_set, closed_set, cost, father, sc)
    # TODO: Implement A* algorithm using open_set, closed_set, and father
    """ raise NotImplementedError('Not implemented') """
