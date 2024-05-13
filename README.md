Synchronization Script Documentation

Overview:
This Python script facilitates the synchronization of data from a source folder or file to a replica folder or file at specified intervals using the command line. It utilizes the argparse module to handle command-line arguments for specifying the source, replica, and synchronization interval.
Modules Used:


•	json: Provides functions for encoding and decoding JSON data.

•	sched: Implements a generic event scheduler for running tasks at specified times.

•	logging: Facilitates logging messages to a file.

•	datetime: Offers classes for manipulating dates and times.

•	argparse: Simplifies the process of parsing command-line arguments.

•	time: Provides various time-related functions.


Functions:
1.	setup_logging(): Sets up logging configuration to log synchronization events to a file named "logs.txt".
2.	synchronize(source, replica): Synchronizes data from a source file or folder to a replica file or folder. It reads data from the source and writes it to the replica using binary mode.
3.	schedule_sync(source, replica, interval, scheduler): Schedules synchronization at a given interval. It invokes the synchronize() function and reschedules itself to run again after the specified interval.
4.	main(): Entry point of the script. Parses command-line arguments using argparse, sets up logging, initializes the scheduler, and schedules the synchronization task. Handles KeyboardInterrupt to gracefully exit the program.
Command-line Arguments:
•	source: Path to the source file or folder to be synchronized.
•	replica: Path to the replica file or folder where data will be synchronized.
•	-i, --interval: Optional argument to specify the synchronization interval in seconds. Default is 60 seconds.
Usage

•	First call will be the pythonfile, First Argument will be the sourcefile, second argument the destination file and the third the call of the function interval(-i) made in seconds.
