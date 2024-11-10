# Task manager
## it's a CLI(Command Line Interface) task manager  
you can use it for managing your tasks. 

there's actually nothing to install, just download and launch "task manager.py"
don't worry, it will create a "data.json" file

## **ATTENTION!!!**
it's allows few commands, such as:
1. `add <text>` - add task with `<text>` description
2. `update <task id> <new description>` - update exist `<task id>` task, by changing it's description on `<new description>`
3. `delete <task id>` - delete `<task id>` task from list
4. `markinprogress` <task id> - will change `<task id>`  status from any to "In progress"
5. `markdone <task id>` - will change `<task id>` status from any to "Done"
6. `marktodo <task id>` - will return status "To do" for `<task id> `
7. `list <!optionally! status>` - display task list with all information, if `<!optionally! status>` is not empty displayed tasks will be filtered by `<!optionally! status>`
## `<!optionally! status>` can be:
1. "to do"
2. "in progress"
3. "done"
   
**ATTENTION!!!** you should use only this names, you can's write "Done", "In_progress", "TODO" or something like this

