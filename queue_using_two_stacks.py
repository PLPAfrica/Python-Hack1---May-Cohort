from queue import QueueWithStacks

def manage_print_jobs() -> str:
    """
    Manage a print job queue using two stacks with user input.

    Methods:
        enqueue(job_id: int): Adds a print job to the queue.
        dequeue() -> int: Removes and returns the front print job.

    Returns:
        str: Summary of print job processing.

     Sample Output:
       Enter print job ID (or 'done' to finish adding jobs): 101
       Enter print job ID (or 'done' to finish adding jobs): 102
       Enter print job ID (or 'done' to finish adding jobs): 103
       Enter print job ID (or 'done' to finish adding jobs): done
       Print Job Management Summary:
       Printing job ID: 101
       Printing job ID: 102
       Printing job ID: 103
       Is the print job queue empty? True 
    """
    job_queue = QueueWithStacks()

    def add_print_jobs():
        """
        Add print jobs to the queue based on user input.
        """
        while True:
            job = input("Enter print job ID (or 'done' to finish adding jobs): ")
            if job.lower() == 'done':
                break
            try:
                job_id = int(job)
                job_queue.enqueue(job_id)
            except ValueError:
                print("Invalid input. Please enter a valid integer job ID or 'done' to finish.")

    def process_print_jobs() -> str:
        """
        Process all print jobs in the queue and return the results.

        Returns:
            str: A string of results showing processed jobs and whether the queue is empty or not.
        """
        results = []
        while not job_queue.empty():
            results.append(f"Printing job ID: {job_queue.dequeue()}")
        results.append(f"Is the print job queue empty? {job_queue.empty()}")
        return "\n".join(results)

    # Add print jobs
    add_print_jobs()

    # Process print jobs and collect results
    summary = process_print_jobs()

    return summary

def create_print_job_summary() -> str:
    """
    Create a summary of print jobs processed by the QueueWithStacks.

    Returns:
        str: A summary report of print job management.
    """
    summary = manage_print_jobs()
    return f"Print Job Management Summary:\n{summary}"

# Test
if __name__ == "__main__":
    print(create_print_job_summary())
