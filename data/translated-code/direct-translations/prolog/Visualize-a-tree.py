from tkinter import Tk, ttk

def display_tree(direction):
    root = Tk()
    root.title(f"Display tree {direction}")
    tree = ttk.Treeview(root)
    tree.insert("", "end", text="Root")
    tree.pack()
    
    child1 = tree.insert("", "end", text="Child1")
    child2 = tree.insert("", "end", text="Child2")
    
    grandchild1 = tree.insert(child1, "end", text="Grandchild1")
    grandchild2 = tree.insert(child1, "end", text="Grandchild2")
    
    grandchild3 = tree.insert(child2, "end", text="Grandchild3")
    grandchild4 = tree.insert(child2, "end", text="Grandchild4")
    
    root.mainloop()

# Example usage:
display_tree("horizontal")