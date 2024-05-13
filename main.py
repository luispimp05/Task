import json
import sched
import logging
import datetime
import argparse
import time


def setup_logging():
    "cofig to the logsfile"
    log_file = "logs.txt"
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s', filemode='a+')


def synchronize(source, replica):
    """Sync data from source to replica."""
    try:

        # Open source file for reading binary data
        with open(source, 'rb') as file:
            source_data = file.read()

        # Open replica file for writing binary data
        with open(replica, 'wb') as replica_file:
            replica_file.write(source_data)

            # Log and print synchronization completion message
            logging.info(f"Synchronized data from '{source}' to '{replica}'")
            print(f"Synchronization completed: {datetime.datetime.now()}")
            
    except Exception as e:

        # Log error if synchronization fails
        logging.error(f"Error occurred during synchronization: {str(e)}")


def schedule_sync(source, replica, interval, scheduler):
    """Schedule synchronization at a given interval."""
    # Call synchronize function
    synchronize(source, replica)
    # Schedule the next synchronization
    scheduler.enter(interval, 1, schedule_sync, (source, replica, interval, scheduler))


def main():
     # Parse command-line arguments    
    parser = argparse.ArgumentParser(description="Sync data from source to replica at a given interval")
    parser.add_argument("source", help="Path to the source file or folder")
    parser.add_argument("replica", help="Path to the replica file or folder")
    parser.add_argument("-i", "--interval", type=int, default=60, help="Synchronization interval in seconds (default is 60)")
    args = parser.parse_args()
    # Setup logging
    setup_logging()
    # Extract arguments
    source = args.source
    replica = args.replica
    interval = args.interval
    # Create a scheduler
    scheduler = sched.scheduler(time.time, time.sleep)
    # Schedule the first synchronization
    scheduler.enter(interval, 1, schedule_sync, (source, replica, interval, scheduler))

    try:
        # Run the scheduler
        scheduler.run()
    except KeyboardInterrupt:
        # Handle keyboard interrupt
        print("Exiting...")


if __name__ == "__main__":
    main()
