"""
Drew Byford
CSD-325
Module 10 - GUI ToDo

This program creates a graphical To-Do list using Python's Tkinter
library. The user can add tasks by typing them into the text box and
pressing Enter. Tasks can be deleted by right-clicking them. The
program also provides a File menu with an Exit option.
"""

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    """Create and manage the GUI To-Do application."""

    def __init__(self, tasks=None):
        """Initialize the To-Do window and its widgets."""
        super().__init__()

        # Create an empty task list if no tasks were provided.
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Set the required window title and size.
        self.title("Byford-ToDo")
        self.geometry("400x450")

        # Create the File menu and Exit option.
        self.menu_bar = tk.Menu(self)

        self.file_menu = tk.Menu(
            self.menu_bar,
            tearoff=0,
            bg="navy",
            fg="white"
        )

        self.file_menu.add_command(
            label="Exit",
            command=self.destroy
        )

        self.menu_bar.add_cascade(
            label="File",
            menu=self.file_menu
        )

        self.config(menu=self.menu_bar)

        # Create the canvas and frames.
        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(
            self.tasks_canvas
        )

        self.text_frame = tk.Frame(self)

        # Create the vertical scrollbar.
        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        # Create the text box where the user enters tasks.
        self.task_create = tk.Text(
            self.text_frame,
            height=3,
            bg="white",
            fg="black"
        )

        # Place the canvas and scrollbar.
        self.tasks_canvas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1
        )

        self.scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        # Place the task frame inside the canvas.
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        # Place the task entry area at the bottom.
        self.task_create.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.text_frame.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        # Put the cursor in the task entry area.
        self.task_create.focus_set()

        # Create the instruction label.
        todo1 = tk.Label(
            self.tasks_frame,
            text="Add items below - Right-click a task to delete",
            bg="navy",
            fg="white",
            pady=10
        )

        # Right-click the instruction/task label to delete it.
        todo1.bind(
            "<Button-3>",
            self.remove_task
        )

        self.tasks.append(todo1)

        # Display existing tasks.
        for task in self.tasks:
            task.pack(
                side=tk.TOP,
                fill=tk.X
            )

        # Set up event bindings.
        self.bind(
            "<Return>",
            self.add_task
        )

        self.bind(
            "<Configure>",
            self.on_frame_configure
        )

        # Mouse wheel bindings for Windows/macOS and Linux.
        self.bind_all(
            "<MouseWheel>",
            self.mouse_scroll
        )

        self.bind_all(
            "<Button-4>",
            self.mouse_scroll
        )

        self.bind_all(
            "<Button-5>",
            self.mouse_scroll
        )

        self.tasks_canvas.bind(
            "<Configure>",
            self.task_width
        )

        # Complementary colors used for alternating tasks.
        self.colour_schemes = [
            {
                "bg": "navy",
                "fg": "white"
            },
            {
                "bg": "orange",
                "fg": "black"
            }
        ]

    def add_task(self, event=None):
        """Add a new task entered by the user."""
        task_text = self.task_create.get(
            1.0,
            tk.END
        ).strip()

        # Do not allow blank tasks.
        if len(task_text) > 0:
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10
            )

            # Apply the alternating color scheme.
            self.set_task_colour(
                len(self.tasks),
                new_task
            )

            # Right-click a task to delete it.
            new_task.bind(
                "<Button-3>",
                self.remove_task
            )

            new_task.pack(
                side=tk.TOP,
                fill=tk.X
            )

            self.tasks.append(new_task)

        # Clear the task entry area.
        self.task_create.delete(
            1.0,
            tk.END
        )

    def remove_task(self, event):
        """Ask for confirmation and remove the selected task."""
        task = event.widget

        if msg.askyesno(
            "Really Delete?",
            "Delete " + task.cget("text") + "?"
        ):
            self.tasks.remove(
                event.widget
            )

            event.widget.destroy()

            # Reapply colors after deletion.
            self.recolour_tasks()

    def recolour_tasks(self):
        """Reapply alternating colors to all remaining tasks."""
        for index, task in enumerate(self.tasks):
            self.set_task_colour(
                index,
                task
            )

    def set_task_colour(self, position, task):
        """Set the appropriate alternating color for a task."""
        _, task_style_choice = divmod(
            position,
            2
        )

        my_scheme_choice = self.colour_schemes[
            task_style_choice
        ]

        task.configure(
            bg=my_scheme_choice["bg"]
        )

        task.configure(
            fg=my_scheme_choice["fg"]
        )

    def on_frame_configure(self, event=None):
        """Update the scrollable area when the frame changes."""
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    def task_width(self, event):
        """Keep task labels the same width as the canvas."""
        canvas_width = event.width

        self.tasks_canvas.itemconfig(
            self.canvas_frame,
            width=canvas_width
        )

    def mouse_scroll(self, event):
        """Scroll the task list using the mouse wheel."""
        if event.delta:
            self.tasks_canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )
        else:
            # Linux uses Button-4 and Button-5 for scrolling.
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(
                move,
                "units"
            )


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()