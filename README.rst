findProcessOwner
================

An application which scans a list of given pids and determines the executing user.


Each line on stdout contains the result, either a username or a uid (if --uid is specified, or a username cannot be determined from a uid), or "unknown" on complete failure (like invalid PID).

Error messages are on the same line, but in stderr, such that any script can use the stdout result and simply check for "unknown" instead of needing to parse the errors.


**Usage**


	Usage: findProcessOwner (options) [pid1] (optional: pid2, pid3)


	Prints the owner (account running) processes, given their pids. They are returned one per line on stdout.

	 Any errors reported go to stderr. If no owner can be determined, stdout will contain "unknown" for that line.

	 Thus your program can always ensure parsable output by parsing stdout, one-entry per line, and checking for "unknown".


	 If a username can not be determined (like user deleted, or uid changed, etc) a pid will be printed.


		Options:


		   \-\-uid                  Print the UID instead of the username

		   \-\-version              Print the version




	Examples:

	  findProcessOwner 1234

	  findProcessOwner \-\-uid 1234 3231


	Return:

	  Returns zero if all searches were successful, otherwise non-zero.




**Examples**


Current shell user:

	$] findProcessOwner $$

	myuser


Three processes, two invalid:

	$] findProcessOwner 12345 $$ 12233

	unknown (Could not determine owner of pid 12345)

	myuser

	unknown (Could not determine owner of pid 12233)


Three processes, two invalid, stderr nullified:

	$] findProcessOwner 12345 $$ 12233 2>/dev/null

	unknown 

	myuser

	unknown 

