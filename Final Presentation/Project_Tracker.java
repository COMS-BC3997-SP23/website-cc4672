import java.util.ArrayList;

// Define a Task class to hold task information
class Task {
    String name;
    String description;
    String priority;
    
    public Task(String name, String description, String priority) {
        this.name = name;
        this.description = description;
        this.priority = priority;
    }
    
    @Override
    public String toString() {
        return "Task: " + name + "\nDescription: " + description + "\nPriority: " + priority + "\n";
    }
}

// Define a TaskManager class to manage tasks
class TaskManager {
    ArrayList<Task> tasks;
    
    public TaskManager() {
        tasks = new ArrayList<Task>();
    }
    
    public void addTask(Task task) {
        tasks.add(task);
        System.out.println("Task added successfully!");
    }
    
    public void removeTask(String taskName) {
        for (Task task : tasks) {
            if (task.name.equals(taskName)) {
                tasks.remove(task);
                System.out.println("Task removed successfully!");
                return;
            }
        }
        System.out.println("Task not found.");
    }
    
    public void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks found.");
        } else {
            for (Task task : tasks) {
                System.out.println(task);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a TaskManager instance
        TaskManager taskManager = new TaskManager();
        
        // Add some sample tasks
        taskManager.addTask(new Task("Finish homework", "Complete math assignment and study for quiz", "High"));
        taskManager.addTask(new Task("Buy groceries", "Get milk, bread, and eggs", "Medium"));
        taskManager.addTask(new Task("Do laundry", "Wash clothes and fold them", "Low"));
        taskManager.addTask(new Task("Write Proposal","Write the research project proposal for Econ","High"));
        
        // View all tasks
        System.out.println("Here are all the tasks: "); 
        taskManager.viewTasks();
    }
}
