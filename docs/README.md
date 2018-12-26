# Focus Phase

Focus Phase (FP) is a simple yet powerful timer and time tracker. It is a command-line application written in Python and can be installed with one command. 

![](FP-header-img.jpg)

FP has two timers: one for when you know for how long you are going to work (like a Pomodoro timer), and the other for when you don't know in advance for how long you are going to work. FP keeps a log of all your work in a csv file on your device. FP allows you to see statistics and graphs about your previous work also.

<a><img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" width=50 /></a>

📄 Below is an explanation on how to install and use FP.

## How to install?

Install easily with `pip`:

```shell
pip3 install fcs
```

This will install FP dependencies if not already installed.

## Topics and tags

FP uses "topics". A **topic** is a thing that you spend time working on. For example, when you want to work on a project called "abc" for 25 minutes, then you add the topic "abc" to FP (see below) then start the timer with the command 

```shell
fcs abc 25
```

If you want to work on "xyz", then add it to FP topics then run

```shell
fcs xyz 25
```

That's it. To give you more flexibility, FP implements **tags**. So, for example, if you want to work on "abc" and "abc" is a web-development project, then you can run 

```shell
fcs abc 25 [web-dev]
```

The previous examples are just one way to use FP. You can combine topics and tags and adapt them to your needs.

## How to add topics?

Before you work on a topic for the first time, you must add it to FP topics easily with the command 

```shell
fcs -a
```

After that, you can start timers to work on that topic. To make things easier, when you add a topic, FP will ask you for its abbreviation to make typing it faster later. 

For example, if you have a topic named "x website front-end development", then instead of typing all of this every time you want to work, you might just type "xfd". 

## Usage

There are three usage modes: two are timers and one is for configuration and statistics. 

> Items enclosed between square brackets are optional.    

### Undetermined timer

```shell
fcs TOPIC_ABBREVIATION [-c][[TAG1,TAG2,...]]
```

The first mode of the timer: undetermined timer. Enter a topic abbreviation to start a timer that will stop when you press the keyboard interrupt keys (`Ctrl + C`).    If `-c` is present in the command, pressing the keyboard interrupt keys will make the user choose whether he wants to stop or pause the timer.    

Tags are optional. If they exist, they should be put inside square brackets (`[` and `]`), **they must be separated by only a comma (`,`), and they must not contain any spaces**. A valid example is `[TAG1,TAG2]`. An invalid example is `[TAG1, TAG2]` (notice the space).   

### Predetermined timer

```shell
fcs TOPIC_ABBREVIATION TIME [[TAG1,TAG2,...]]
```

The second mode of the timer: predetermined timer. To start a timer, enter a topic abbreviation and the number of minutes you want to work on that topic. You can stop or pause this timer by pressing the keyboard interrupt keys (`Ctrl + C`). 

### Statistics, visualization, and configuration

```shell
fcs FUNCTION [PARAMETERS] 
```

where FUNCTION can be one of the following:   

| Function                    | Description                                                  |
| :-------------------------- | :----------------------------------------------------------- |
| --add-topics, -a            | to add new topics                                            |
| --deletetopics, -d          | to delete topics (will not delete entries in the log related to the deleted topic) |
| --showtopics, -st           | to show all topics with their abbreviations                  |
| --deletealltopics, -da      | to delete all topics                                         |
| --showtags, -sta            | to show all tags used in all entries in the log              |
| --clearlog, -cl             | to delete all entries from the log file                      |
| --showlog, -sl              | to display a formatted table of the log entries              |
| --showlog:N, -sl:N          | to display a table of a selected info about the last N log entries |
| --backup, -b                | to create a backup of the log file and the topic file        |
| --today [TOPIC], -t [TOPIC] | to display the total time spent on TOPIC today. If TOPIC is not provided, total time spent today on all topics is calculated |
| --calc, -cal                | to calculate time spent on all topics, on a specified topic, or on a specified tag |
| --addentry, -ae             | to manually add an entry (not recommended for now)           |
| --deletelast, -dl           | to delete the last entry in the log                          |
| --visual, -v                | to see a visualization of the work done on a topic, the work done on all topics, or the work done on a certain tag over the last 30 days |

## Examples

### 1. Predetermined timer

If you want to work for 30 minutes on a building a web application named "xy zw" using Vue.js framework, then you should add this topic first (if this is your first time working on it):

```shell
fcs -a
```

The program will ask you for a topic abbreviation and a topic full name. Suppose that you entered "xyzw" for the abbreviation and "xy wz web application" for the full name. Then you start the timer with:

```shell
fcs xyzw 30 [web-dev,vue.js]
```

This will start a *predetermined* timer for 30 minutes, and it will save the session entry with the tags "web-dev" and "vue.js".

### 2. Undetermined timer

If you want to work on a building a web application named "xy zw" using Vue.js framework, then you should add this topic first (if this is your first time working on it):

```shell
fcs -a
```

The program will ask you for a topic abbreviation and a topic full name. Suppose that you entered "xyzw" for the abbreviation and "xy wz web application" for the full name. Then you start the timer with:

```shell
fcs xyzw [web-dev,vue.js]
```

This will start an *undetermined* timer, and it will save the session entry with the tags "web-dev" and "vue.js". To stop the timer, press `Ctrl + C` on the keyboard.

### 3. Statistics

To see for how many minutes you have worked today on the topic "xyzw" that we've added above:

```shell
fcs -t xyzw
```

It will display a message like:

> Today (23-December-2018), 50 minutes have been spent on xy wz web application

To see the time spent on all topics in all days:

```shell
fcs -cal
```

It will show you options to choose from; one of them is to calculate the time spent on all topics in all days.

To see a visualization of your work on "xyzw" topic over the last 30 days:

```shell
fcs -v
```

It will also display options to choose from and one of them achieves what we want in this example.

There are many things you can do. See the usage section for more.

## Focus Phase components    

FP has two main files:

- A log file that keeps information about your previous sessions (like time elapsed, date of the session, etc)   
- A file that contains the names and abbreviations of the topics you work on

## Success Music

When you use the predetermined timer mode, and when you work for the whole specified period, a short music will be played. This feature is available on Mac computers only for now. 

## How to get your data?

Run the backup command `fcs -b` and a message will tell you the path of the folder that contains the backup files. Go and get them from there.

## Notes   

- Date of a session is calculated at the start of the session.      
- Add `-q` to the command to prevent playing sounds (quiet mode)
