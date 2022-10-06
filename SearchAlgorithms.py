from Space import *
from Constants import *


def is_Exist(arr: list[Node], val: Node):
    for i in range(0, len(arr)):
        if arr[i].value == val.value:
            return True

    return False


def set_Color_Path(g: Graph, path: list[Node], sc: pygame.surface):
    for i in range(0, len(path)):
        g.re_draw(path[i], grey, sc)
        # path[i].set_color(grey)


def findMinCost(g: Graph, l: list[Node]):
    min = 99999
    result: Node = l[0]
    for index in l:
        if min > g.calculatorCost(index):
            min = g.calculatorCost(index)
            result = index

    return result


def BFS_algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], sc: pygame.surface):
    if len(open_set) == 0:
        return

    current_List: list[Node] = []
    current_List = current_List + open_set
    while len(current_List) != 0:
        current_Node: Node = current_List[0]
        g.re_draw(current_Node, yellow, sc)
        # kiểm tra xem tìm thấy node cần tìm chưa
        # nếu tìm thấy r => bôi màu rgey đường đi
        # nếu chưa thì kiểm thêm node đang xét vào closed, xóa khỏi open
        # thêm vào open các neighbors của node
        if g.is_goal(current_Node):
            set_Color_Path(g, closed_set, sc)
            return

        # thêm vào closed_set
        open_set.remove(current_Node)
        closed_set.append(current_Node)
        current_List.remove(current_Node)
        g.re_draw(current_Node, blue, sc)
        # current_Node.set_color(blue)

        # thêm vào open_set
        neighbors: list[Node] = g.get_neighbors(current_Node)
        while len(neighbors) != 0:
            if not is_Exist(closed_set, neighbors[0]):
                if not is_Exist(open_set, neighbors[0]):
                    if neighbors[0].value != g.goal.value:
                        g.re_draw(neighbors[0], red, sc)
                    open_set.append(neighbors[0])

            neighbors.remove(neighbors[0])

    BFS_algorithm(g, open_set, closed_set, sc)


def DFS_algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], sc: pygame.surface):
    if len(open_set) == 0:
        return

    # lấy điểm gần nhất được mở tới
    current_Node: Node = open_set[len(open_set) - 1]
    g.re_draw(current_Node, yellow, sc)

    if (g.is_goal(current_Node)):
        set_Color_Path(g, closed_set, sc)
        return

    # xóa điểm đó khỏi tập mở và thêm vào tập đóng
    open_set.remove(current_Node)
    closed_set.append(current_Node)

    # tô lại màu
    g.re_draw(current_Node, blue, sc)

    # tạo ra tập chứa các neighbors
    # thêm vào sau open_set khi điểm đó k có trong open_set và closed_set
    neighbors: list[Node] = g.get_neighbors(current_Node)
    while len(neighbors) != 0:
        if not is_Exist(closed_set, neighbors[len(neighbors) - 1]):
            if not is_Exist(open_set, neighbors[len(neighbors) - 1]):
                if neighbors[0].value != g.goal.value:
                    g.re_draw(neighbors[0], red, sc)
                open_set.append(neighbors[len(neighbors) - 1])

        neighbors.remove(neighbors[len(neighbors) - 1])

    DFS_algorithm(g, open_set, closed_set, sc)


def UCS_algorithm(g: Graph, open_set: list[Node], closed_set: list[Node], sc: pygame.surface):
    if len(open_set) == 0:
        return

    # xác định điểm xét tới
    current_Node: Node = findMinCost(g, open_set)
    g.re_draw(current_Node, yellow, sc)

    # kiểm tra xem điểm đang xét có phải là goal không
    if g.is_goal(current_Node):
        set_Color_Path(g, closed_set, sc)
        return

    # xóa khỏi open_set và thêm vào closed_set
    open_set.remove(current_Node)
    closed_set.append(current_Node)
    g.re_draw(current_Node, blue, sc)

    neighbors: list[Node] = g.get_neighbors(current_Node)
    while len(neighbors) != 0:
        if not is_Exist(closed_set, neighbors[len(neighbors) - 1]):
            if not is_Exist(open_set, neighbors[len(neighbors) - 1]):
                if neighbors[0].value != g.goal.value:
                    g.re_draw(neighbors[0], red, sc)
                open_set.append(neighbors[len(neighbors) - 1])

        neighbors.remove(neighbors[len(neighbors) - 1])

    UCS_algorithm(g, open_set, closed_set, sc)


def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    # nút mở với bắt đầu là điểm bắt đầu
    # tập đóng ???
    # tạo ra 1 array với len = len(g)
    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []

    DFS_algorithm(g, open_set, closed_set, sc)
    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []
    """ father = [-1]*g.get_len() """

    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    BFS_algorithm(g, open_set, closed_set, sc)

    raise NotImplementedError('Not implemented')


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    """ open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0 """

    open_set: list[Node] = []
    open_set.append(g.start)
    closed_set: list[Node] = []

    UCS_algorithm(g, open_set, closed_set, sc)
    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
