try:
    from optparse import OptionParser
    import random
    from tkinter import *
except ImportError as msg:
    print("[!] Library not installed: " + str(msg))
    exit()


class Maze_Creation:

    # Default values
    height = 20
    width = 20
    output = "output_file.txt"
    coords = []
    visited_areas = set()

    def __init__(self):
        try:
            # Parse Arguments
            parser = OptionParser()
            parser.add_option("-n", "--height", action="store",
                              type="string", dest="height", help="The height of maze")
            parser.add_option("-w", "--width", action="store",
                              type="string", dest="width", help="The width of maze")
            parser.add_option("-s", "--seed", action="store", type="string", dest="seed",
                              help="The seed is a number or a string that it is given to generate a random seed for our program.")
            parser.add_option("-o", "--output", action="store_true",
                              dest="output", help="Output file where the coords are stored")

            (options, args) = parser.parse_args()

            # Check arguments
            if len(sys.argv) < 9:
                if options.height is not None:
                    try:
                        self.height = int(options.height)
                    except ValueError:
                        print("[!] You incorrectly defined a non integer for -n")
                    if self.height <= 0:
                        print("[!] Height should not be a negative number")
                        exit(1)
                if options.width is not None:
                    try:
                        self.width = int(options.width)
                    except ValueError:
                        print("[!] You incorrectly defined a non integer for -n")
                    if self.width <= 0:
                        print("[!] Height should not be a negative number")
                        exit(1)
                if options.seed is not None:
                    random.seed(options.seed)

                self.make_maze()

                if options.output == True:
                    self.store()

            # Print help
            else:
                print("[!] More than eligible arguments given")
                print()
                parser.print_help()
                exit()

        # Throw Exceptions
        except IOError as ex:
            print("[!] " + ex.strerror + ": " + ex.filename)
        except KeyboardInterrupt as ex:
            print("[#] Ending procedure...")
            print("[#] Programm aborted")
            exit()

    # Depth First Implementation of Maze Generation
    def make_maze(self):
        # Randomly choose the starting coordinate
        start_x = random.randrange(self.width)
        start_y = random.randrange(self.height)
        self.visited_areas.add((start_x, start_y))
        # Find the possible neighbours
        end = self.neighbours(start_x, start_y)
        # Repeat until there are no more possible nodes
        while not end:
            random_visited = random.sample(
                self.visited_areas, len(self.visited_areas))
            for visited_node in random_visited:
                x, y = visited_node
                end = self.neighbours(x, y)
        self.visualize()

    def neighbours(self, x, y):
        # Visit neighbouring nodes until there are no possible nodes
        exists = True
        while (exists):
            neighbouring_nodes = []
            if x - 1 >= 0:
                neighbouring_nodes.append((x - 1, y))
            if y - 1 >= 0:
                neighbouring_nodes.append((x, y - 1))
            if x + 1 < self.width:
                neighbouring_nodes.append((x + 1, y))
            if y + 1 < self.height:
                neighbouring_nodes.append((x, y + 1))
            random_neighbours = random.sample(
                neighbouring_nodes, len(neighbouring_nodes))
            exists = False
            for neighbour in random_neighbours:
                xx, yy = neighbour
                if (xx, yy) not in self.visited_areas:
                    self.visited_areas.add((xx, yy))
                    self.coords.append([x, y, xx, yy])
                    x = xx
                    y = yy
                    exists = True
                    break
        for i in range(self.width):
            for j in range(self.height):
                if (i, j) not in self.visited_areas:
                    return False
        return True
    
    # Store maze's coordinates in txt file
    def store(self):
        self.file = open(self.output, "w+")
        for c in self.coords:
            self.file.write("(%d, %d), (%d, %d)\n" % (c[0], c[1], c[2], c[3]))

    # Visualize maze
    def visualize(self):
        master = Tk()
        # Create the canvas so that it takes half of the screen
        canvas_width = master.winfo_screenwidth() / 2
        canvas_height = master.winfo_screenheight() / 2
        multw = canvas_width / self.width
        multh = canvas_height / self.height
        mult = min(multh, multw)
        canvas_width = mult * self.width
        canvas_height = mult * self.height
        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        master.geometry("%dx%d+0+0" % (canvas_width, canvas_height))
        master.wm_title("Maze")
        master.iconbitmap(r'maze.ico')
        w.pack()

        # Illustrate the walls
        for c in self.coords:
            w.create_line(c[0] * mult + mult / 2, c[1] * mult + mult / 2,
                          c[2] * mult + mult / 2, c[3] * mult + mult / 2, fill="#476042")
        mainloop()

# Execute Maze_Creation
Maze_Creation()
