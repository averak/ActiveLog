ActiveLog
=======

A simple logging utility for Python.

## Usage
### Description of Constructors's Argument
name                |Description
--------------------|-----------------------------------------------------------------
shift_freq          | frequency of log file rotation. [sec]
shift_size          | file size of log file rotation. [byte]
level               | Logging severity threshold. Default values is logger.DEBUG
init                | Whether to clear log files. [True / False]
datetime_format     | Date and time format. Default value is '%Y-%m-%d %H:%M:%S.%f'.
shift_period_suffix | The log file suffix format for rotation. Default is '_%Y-%m-%d'.

### Simple Example
```python
import activelog

# Create a Logger that prints to STDOUT
log = activelog.Logger(logger.STDOUT)
log.debug("Created Logger")
log.info("Program finished")

# Create a Logger that prints to Log File
log = activelog.Logger('log file path')
log.warn("This is WARN message")
log.error("This is ERROR message")
```

### Log File Shift Example
```python
# Switch log file daily
log = activelog.Logger('log file path', shift_freq=60*60*24)
# Switch log file weekly
log = activelog.Logger('log file path', shift_freq=60*60*24*7)

# Switch log file every 10MB
log = activelog.Logger('log file path', shift_size=100000000)
```

### Output Example
```
[2020-01-01 07:11:09.887267 #sample.py line:4] INFO  -- : Program Start!!
[2020-01-01 07:11:23.535936 #sample.py line:9] ERROR -- : Program End...
```

## Contributing
Bug reports and pull requests are welcome on GitHub at [https://github.com/AjxLab/ActiveLog](https://github.com/AjxLab/ActiveLog).
