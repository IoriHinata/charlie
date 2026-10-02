"""Minimal offline-compatible CHARLIE browser bridge for Pyodide."""
import json

_state = {"awake": True, "experience": 0, "last_command": "boot"}
_logs = ["CHARLIE browser bridge started"]

def browser_tick():
    return browser_snapshot()

def browser_command(command):
    _state["last_command"] = str(command)
    _state["awake"] = command != "sleep"
    if command == "reward":
        _state["experience"] += 1
    _logs.append("command: " + str(command))
    return browser_snapshot()

def browser_snapshot():
    return json.dumps(_state, ensure_ascii=False, indent=2)

def browser_logs():
    return "\n".join(_logs[-100:])

def browser_export_memory():
    return json.dumps(_state, ensure_ascii=False)

def browser_import_memory(memory):
    _state.update(json.loads(memory))
    _logs.append("memory imported")
    return browser_snapshot()
