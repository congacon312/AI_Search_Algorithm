from Constants import *

class Node:
    def __init__(self, x, y, value, radius = 10) -> None:
        '''
        x,y: tọa độ của node
        value: giá trị của node, có thể dùng làm giá trị định danh
        radius: bán kính node
        '''
        self.x, self.y, self.value = x, y, value
        self.radius = radius
        self.color = green



class Graph:
    def __init__(self, start_pos:int, goal_pos:int) -> None:
        '''
        khởi tạo đồ thị
        start_pos: vị trí bắt đầu
        goal_pos: vị trí đích
        các vị trí này chính là giá trị `value` của node
        '''
        self.grid_cells:list[Node] = []
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                self.grid_cells.append(Node(j*TILE+TILE/2, i*TILE+TILE/2, (i-1)*(cols-2)+(j-1)))

        self.start:Node = self.grid_cells[start_pos]
        self.goal:Node = self.grid_cells[goal_pos]

    def get_len(self) -> int:
        '''
        trả về số node của đồ thị
        '''
        return len(self.grid_cells)

    def is_goal(self, node:Node) -> bool:
        '''
        kiểm tra node `node` có phải là đích hay không
        '''
        if node.value == self.goal.value:
            return True
        return False


    def get_neighbors(self, node:Node):
        '''
        trả về các node kề của node `node` theo 8 hướng
        '''
        r = node.value//(cols-2)
        c = node.value%(cols-2)

        up = (r-1, c) if r-1 >= 0 else None
        down = (r+1, c) if r+1 < (rows-2) else None
        left = (r, c-1) if c-1 >= 0 else None
        right = (r, c+1) if c+1 < (cols-2) else None

        up_left = (r-1, c-1) if r-1 >= 0 and c-1 >= 0 else None
        up_right = (r-1, c+1) if r-1 >= 0 and c+1 < (cols-2) else None
        down_left = (r+1, c-1) if r+1 < (rows-2) and c-1 >= 0 else None
        down_right = (r+1, c+1) if r+1 < (rows-2) and c+1 < (cols-2) else None

        directions = [up, down, left, right, up_left, up_right, down_left, down_right]
        neighbors = []
        for dir in directions:
            if dir is not None:
                neighbors.append(self.grid_cells[dir[0]*(cols-2) + dir[1]])
        return neighbors

def is_Exist(arr, val):
    for i in range(0, len(arr)):
        if arr[i] == val:
            return True

    return False


def BFS_algorithm(g: Graph, open_set: [], closed_set: []):
    current_List = open_set
    print(current_List)
    while len(current_List) != 0:
        current_Node = current_List[0]
        # kiểm tra xem tìm thấy node cần tìm chưa
        # nếu tìm thấy r => bôi màu rgey đường đi
        # nếu chưa thì kiểm thêm node đang xét vào closed, xóa khỏi open
        # thêm vào open các neighbors của node
        if current_Node == g.goal.value:
            print("tìm thấy r nha thằng lồn")
            return
        # thêm vào closed_set
        open_set.remove(current_Node)
        closed_set.append(current_Node)
        current_List.remove(current_List[0])

        # thêm vào open_setz
        neighbors = current_Node.get_neighbors()
        while len(neighbors) != 0:
            if not is_Exist(closed_set, neighbors[0]):
                if not is_Exist(open_set, neighbors[0]):
                    open_set.append(neighbors[0])

            neighbors.remove(neighbors[0])

    BFS_algorithm(g, open_set, closed_set)


def DFS(g: Graph):
    print('Implement DFS algorithm')

    # nút mở với bắt đầu là điểm bắt đầu
    open_set = [g.start.value]
    # tập đóng ???
    closed_set = []
    # tạo ra 1 array với len = len(g)
    father = [-1]*g.get_len()

    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def BFS(g: Graph):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    print(open_set)
    closed_set = []
    father = [-1]*g.get_len()

    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    BFS_algorithm(g, open_set, closed_set)

    raise NotImplementedError('Not implemented')


def UCS(g: Graph):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def AStar(g: Graph):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


g = Graph(71, 231)
print(g)